# Modified by Acrazie on 2026-11-03 for the independent EGM fork.
# Copyright 2026 Google LLC.
# SPDX-License-Identifier: Apache-2.0

"""Offline contracts for the adaptive interface, not model-behavior proof."""

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
PUBLIC_SKILLS = {"egm-design", "egm-review", "egm-drift-report", "egm-bootstrap"}
RETIRED = {"egm-brainstorm", "egm-draft", "egm-resolve", "egm-review-loop"}


def test_public_surface_is_exact_and_explicit_only() -> None:
  skills = list((ROOT / "skills").glob("*/SKILL.md"))
  assert {path.parent.name for path in skills} == PUBLIC_SKILLS
  for path in skills:
    metadata = yaml.safe_load(path.read_text().split("---", 2)[1])
    assert metadata["name"] == path.parent.name
    assert metadata["disable-model-invocation"] is True
    interface = yaml.safe_load((path.parent / "agents/openai.yaml").read_text())
    assert interface["policy"]["allow_implicit_invocation"] is False
  personas = {
      yaml.safe_load(path.read_text().split("---", 2)[1])["name"]
      for path in (ROOT / "agents").glob("*.md")
  }
  assert not PUBLIC_SKILLS.intersection(personas)
  assert all(not (ROOT / "skills" / name).exists() for name in RETIRED)


def test_design_and_review_share_one_review_owner() -> None:
  for skill in ("egm-design", "egm-review"):
    body = (ROOT / "skills" / skill / "SKILL.md").read_text()
    assert "resources/review-workflow.md" in body
    assert "resources/execution_instructions.md" in body
  workflow = (ROOT / "resources/review-workflow.md").read_text()
  for requirement in ("reviewed revision", "not run", "fresh", "accepted risks",
                      "targeted revalidation", "human", "temporary"):
    assert requirement in workflow


def test_host_selection_uses_current_design_reviewer_name() -> None:
  persona = ROOT / "agents/design_critic.md"
  name = yaml.safe_load(persona.read_text().split("---", 2)[1])["name"]
  codex = (ROOT / "docs/codex.md").read_text()
  harnesses = (ROOT / "docs/harnesses.md").read_text()
  muse = (ROOT / "docs/muse.md").read_text()
  assert f"a role such as `{name}` maps to `agents/design_critic.md`" in codex
  assert f"(`{name}`, `egm-zoom-out`" in harnesses
  assert f"definitions (`egm/{name}`" in muse
  assert f"frontmatter, not filename: `{name}` is" in muse


def test_runtime_has_no_retired_command_or_mandatory_report_dependency() -> None:
  paths = [*(ROOT / "skills").rglob("*.md"),
           *(ROOT / "agents").glob("*.md"),
           *(ROOT / "resources").rglob("*.md")]
  for path in paths:
    text = path.read_text()
    for retired in RETIRED:
      assert retired not in text, (path, retired)
    for artifact in ("concepts_brief.md", "design_draft.md", "zoom_out_report.md",
                     "goldfish_review_report.md", "consolidated_review_report.md"):
      assert artifact not in text, (path, artifact)


def test_scenarios_cover_material_failure_and_resume_paths() -> None:
  scenarios = yaml.safe_load(
      (ROOT / "skills/egm-design/test_scenarios.yaml").read_text())["scenarios"]
  ids = {scenario["scenario_id"] for scenario in scenarios}
  assert {"raw_idea", "existing_design", "draft_only", "resume_new_session",
          "structural_choice", "reviewer_failure", "no_source_writes",
          "approved_intent_conflict"} <= ids


def test_drift_does_not_require_exhaustive_code_documentation() -> None:
  text = (ROOT / "skills/egm-drift-report/SKILL.md").read_text()
  assert "Undocumented code alone is not drift" in text
  assert "without" in text and "report file" in text
