# Copyright 2026 Google LLC.
# SPDX-License-Identifier: Apache-2.0

"""Offline regression tests for Codex command-read trace evidence."""

from pathlib import Path
import runpy
import shlex
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.parametrize(
    ("parsed_command", "exit_code", "output", "expected"),
    [
        (
            lambda path: {
                "type": "unknown",
                "cmd": f"cat {shlex.quote(path)} "
                       f"{shlex.quote(str(Path(path).with_name('missing')))}",
            },
            1,
            "# Installed guide\n" + "guide content " * 20,
            True,
        ),
        (
            lambda path: {
                "type": "unknown",
                "cmd": f"pwd; rg --files -g 'README*' .; cat {shlex.quote(path)}",
            },
            0,
            "# Installed guide\n" + "guide content " * 20,
            True,
        ),
        (
            lambda path: {
                "type": "unknown",
                "cmd": f"cd {shlex.quote(str(Path(path).parent))} && cat {shlex.quote(path)}",
            },
            0,
            "# Installed guide\n" + "guide content " * 20,
            False,
        ),
        (
            lambda path: {
                "type": "unknown",
                "cmd": f"cat {shlex.quote(path)} | head",
            },
            0,
            "# Installed guide\n" + "guide content " * 20,
            False,
        ),
        (
            lambda path: {
                "type": "unknown",
                "cmd": f"cat {shlex.quote(path)} "
                       f"{shlex.quote(str(Path(path).with_name('missing')))}",
            },
            1,
            "cat: /missing: No such file or directory\n",
            False,
        ),
        (
            lambda path: {"type": "read", "path": str(path)},
            1,
            "# Installed guide\n" + "guide content " * 20,
            False,
        ),
        (
            lambda path: {"type": "read", "path": str(path)},
            0,
            "# Installed guide\n" + "guide content " * 20,
            True,
        ),
    ],
    ids=(
        "failed-cat-printed-file", "compound-cat-printed-file",
        "and-separated-cat-rejected", "piped-cat-rejected",
        "failed-cat-no-file-output", "failed-read", "successful-read",
    ),
)
def test_successful_reads_requires_native_trace_evidence(
    tmp_path: Path, parsed_command, exit_code: int, output: str,
    expected: bool,
) -> None:
    successful_reads = runpy.run_path(
        str(ROOT / "tests/integration/test_codex.py")
    )["successful_reads"]
    guide = tmp_path / "docs" / "codex.md"
    guide.parent.mkdir()
    guide.write_text("# Installed guide\n" + "guide content " * 20)
    command = parsed_command(str(guide))
    trace = [{
        "type": "event_msg",
        "payload": {
            "type": "item_completed",
            "item": {
                "type": "CommandExecution",
                "status": "failed" if exit_code else "completed",
                "exit_code": exit_code,
                "cwd": tmp_path.as_uri(),
                "parsed_cmd": [command],
                "aggregated_output": output,
            },
        },
    }]

    assert (guide.resolve() in successful_reads(trace)) is expected


@pytest.mark.parametrize(
    ("prefix", "suffix", "expected"),
    [
        ("", "", True),
        ("cd elsewhere; ", "", False),
        ("cd elsewhere && ", "", False),
        ("", " | head", False),
        ("", "\nprintf ignored", False),
    ],
    ids=("standalone", "changed-cwd", "conditional", "pipe", "newline"),
)
def test_compound_cat_with_mixed_paths(
    tmp_path: Path, prefix: str, suffix: str, expected: bool,
) -> None:
    successful_reads = runpy.run_path(
        str(ROOT / "tests/integration/test_codex.py")
    )["successful_reads"]
    cwd = tmp_path / "workspace with spaces"
    cwd.mkdir()
    persona = tmp_path / "persona.md"
    persona.write_text("# Reviewer persona\nIndependent review instructions.\n")
    target = cwd / "design with spaces.md"
    target.write_text("# Design\nOrdering must be preserved.\n")
    command = f"{prefix}cat {shlex.quote(str(persona))} {shlex.quote(target.name)}{suffix}"
    trace = [{
        "type": "event_msg",
        "payload": {
            "type": "item_completed",
            "item": {
                "type": "CommandExecution",
                "status": "completed",
                "exit_code": 0,
                "cwd": cwd.as_uri(),
                "parsed_cmd": [{"type": "unknown", "cmd": command}],
                "aggregated_output": persona.read_text() + target.read_text(),
            },
        },
    }]

    assert successful_reads(trace) == (
        {persona.resolve(), target.resolve()} if expected else set()
    )


def test_isolation_run_does_not_require_plugin_discovery(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    run_codex = runpy.run_path(
        str(ROOT / "tests/integration/test_codex.py")
    )["run_codex"]
    trace = [{"type": "event_msg", "payload": {"type": "task_complete"}}]

    def fake_run(command, **kwargs):
        kwargs["stdout"].write(
            '{"type":"thread.started","thread_id":"isolation-probe"}\n'
            '{"type":"turn.completed"}\n'
        )
        return SimpleNamespace(returncode=0)

    def fake_read_trace(thread_id):
        assert thread_id == "isolation-probe"
        return trace

    monkeypatch.setitem(run_codex.__globals__, "subprocess", SimpleNamespace(run=fake_run))
    monkeypatch.setitem(run_codex.__globals__, "read_trace", fake_read_trace)
    workspace = tmp_path / "probe"
    workspace.mkdir()
    installed = ("egm@test", "test", tmp_path / "marketplace", tmp_path / "plugin")

    assert run_codex(installed, workspace, "Check parent-turn isolation only.") == trace
