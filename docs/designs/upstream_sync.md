# Synchronisation du fork avec `google/elephant-goldfish-model@70406c4`

Statut : brouillon révisé suite à la première passe de revue indépendante ; revalidation ciblée requise avant approbation humaine.

## Objectif et périmètre

Synchroniser le fork indépendant `Acrazie/elephant-goldfish-model` (actuellement sur `main` @ `fcb2b62`, 3 PRs au-dessus de l'ancêtre commun `464db03`) avec `google/elephant-goldfish-model@70406c4` (60 commits upstream, 250 fichiers modifiés, dont 100 en chevauchement avec le fork) via un merge Git unique dans une branche dédiée, tout en préservant l'ensemble des invariants produit, architecturaux et d'identité du fork.

Le succès est atteint lorsqu'un agent d'implémentation (sous mandat séparé) peut exécuter le merge dans un ordre sûr, résoudre chaque catégorie de conflit de manière déterministe sans ambiguïté sur les contrats publics, et prouver l'intégrité du fork (tests unitaires, packaging, site Astro, linters et vérifications de non-régression).

### Objectifs (Goals)

- Fusionner `google/elephant-goldfish-model@70406c4` via un merge commit unique dans une branche de sync (`sync/upstream-70406c4`) sans réécrire l'historique de `main`.
- Préserver intégralement les apports du fork : workflow adaptatif `egm-design` (PR #1), contrat `Definition of Done` et portes de livraison (PR #3), correctif de validation des traces Codex (PR #2), identité indépendante (`NOTICE`, manifests Acrazie en version `0.1.0`, en-têtes de modification).
- Intégrer le reviewer TRIZ `egm-inventive-catalyst` (`#299`) comme spécialiste optionnel dans le workflow de revue du fork (`resources/review-workflow.md` et `skills/egm-review/SKILL.md`) et l'enregistrer sur tous les harnesses supportés (Claude, Cursor, Copilot, OpenCode).
- Adopter la suppression du répertoire commité `distributions/claude/` (`#393`) et la dérivation dynamique du runtime Claude dans `scripts/pack_plugin.py` (`#394`), en conservant l'identité et `NOTICE` du fork.
- Adopter la refonte complète de `site/` et `docs/site/` (architecture docs Astro, composants, accessibilité, mise à jour Astro 7.4.12) en réécrivant les pages de contenu et fixtures de test pour la surface de skills du fork (`egm-design`, `egm-review`, `egm-bootstrap`, `egm-drift-report`) et les URLs du dépôt `Acrazie/elephant-goldfish-model`.
- Intégrer les correctifs techniques et améliorations CI génériques : détection `.NET` / extensions `egm-bootstrap` (`#324`, `#409`), fixes packaging/manifests (`#296`, `#311`, `#336`, `#347`, `#377`), sauvegarde des URLs `GoldfishContext` portée sur `egm-review` (`#289`), correctif Codex Windows/sortie vide (`#297`) combiné à PR #2, durcissement `pr-scope-advisory.yml` (`#341`), bundle de provenance générique `release.yml` (`#426`), timeouts (`#424`), lint Python/workflows (`#427`) et bumps de dépendances (`#339`, `#362`, `#384`, `#440`).

### Hors périmètre (Non-Goals)

- **Exclure l'adaptateur Windsurf** (`#407`, `#379`) : ne pas conserver `.windsurf/`, `docs/designs/windsurf_support.md`, `tests/unit/test_windsurf.py` ni ses références dans `scripts/pack_plugin.py`, les tests ou la documentation.
- **Exclure le protocole `egm-lite`** (`#419`, `#438`) : ne pas conserver `skills/egm-lite/`, `docs/designs/lite.md`, `docs/site/skills/egm-lite.md` ni ses références dans `scripts/pack_plugin.py`, `site/` ou les tests.
- **Exclure la gouvernance et le branding spécifiques à Google** : ne pas adopter `.github/CODEOWNERS` vers `@google/egm-maintainers` (`#340`), l'auteur `Google LLC` dans les manifests (`#466`), le bump de version directory Google `0.1.1` (`#316`), la configuration Gemini Code Assist (`.gemini/` `#320`), le workflow de triage PR Google-only (`.github/workflows/pr-triage-review.yml`, `.github/scripts/review_pr.py`, `tests/unit/test_pr_triage_review.py` `#380`/`#413`/`#439`) ni `.github/workflows/scorecard.yml` (`#425`).
- **Ne pas réintroduire les 4 skills retirés par le fork** (`egm-brainstorm`, `egm-draft`, `egm-resolve`, `egm-review-loop`) ni les rapports obligatoires supprimés par PR #1.
- Aucune exécution de code, aucun commit, push, merge sur `main` ou ouverture de PR dans le cadre de ce document de design.

## Décisions architecturales retenues

1. **Stratégie Git — Merge commit unique depuis `upstream/main` (`70406c4`)** :
   - *Choix* : Fetcher `70406c4` depuis `https://github.com/google/elephant-goldfish-model.git`, créer `sync/upstream-70406c4` depuis `main` (`fcb2b62`), exécuter `git merge --no-commit --no-ff 70406c4`, nettoyer immédiatement les ajouts exclus auto-stagés, résoudre les conflits selon la matrice ci-dessous puis valider le merge commit (sous mandat d'implémentation).
   - *Justification* : Maintient un ancêtre commun Git exact (`70406c4`) pour réduire le coût des futures synchronisations sans réécrire l'historique public de `main`.
   - *Alternative écartée* : Cherry-pick sélectif (perd l'ancêtre commun et force la re-résolution des mêmes 60 commits à chaque future synchro).

2. **Intégration sélective des fonctionnalités upstream** :
   - **Retenu** : `egm-inventive-catalyst` (TRIZ, `#299`) comme spécialiste optionnel invoqué lorsque le design comporte une contradiction technique ou un compromis architectural non résolu. Il ne rend pas obligatoire une passe brainstorm ni une boucle 6-lenses.
   - **Écartés** : Windsurf (`#379`, `#407`) et `egm-lite` (`#419`, `#438`), afin d'éviter une surface de maintenance supplémentaire et un recouvrement avec `egm-design` qui est déjà adaptatif.

3. **Suppression de `distributions/claude/` et refonte de `site/`** :
   - **Suppression de `distributions/claude/` (`#393`, `#394`)** : Élimine la duplication manuelle des fichiers entre la racine et `distributions/claude/`. Le runtime Claude est dérivé dynamiquement par `scripts/pack_plugin.py` à partir des sources racine du fork.
   - **Adoption de la refonte `site/`** : Aligne la stack technique (`Astro 7.4.12`, pipeline `docs/site/*.md`, accessibilité, tests `site/scripts/check-docs.mjs`) tout en réécrivant les pages de documentation et les fixtures de test pour refléter exactement les 4 skills publics du fork et le dépôt `Acrazie/elephant-goldfish-model`.

4. **Version des manifests et descripteur Cursor marketplace** :
   - **Version publique fixée à `0.1.0`** : Conserver uniformément `"version": "0.1.0"` dans tous les manifests versionnés (`plugin.json`, `.plugin/plugin.json`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json` et le manifest Copilot `#311`). Le bump upstream `0.1.1` (`#316`) correspond à la soumission directory Google et ne doit pas modifier la numérotation indépendante du fork. (`.claude-plugin/marketplace.json` et `.agents/plugins/marketplace.json` ne portent pas de champ `version`.)
   - **Conserver `.cursor-plugin/marketplace.json` (`#377`)** : L'adopter et l'adapter à l'identité du fork (`Acrazie`, `https://github.com/Acrazie/elephant-goldfish-model`), par cohérence avec `.claude-plugin/marketplace.json` et `.agents/plugins/marketplace.json`.

5. **Séparation stricte CI générique vs gouvernance Google** :
   - **Adopter intégralement** les améliorations CI génériques et de sécurité : durcissement `pull_request_target` sur `.github/workflows/pr-scope-advisory.yml` (`#341` : ajout de `branches: [main]`, `timeout-minutes: 5`, suppression de la permission `contents: read` inutile), provenance générique `actions/attest` (`egm-$RELEASE_TAG.intoto.jsonl`) sur `.github/workflows/release.yml` (`#426`, accompagnée de la mise à jour du slug dépôt dans `scripts/prepare_release.py` vers `Acrazie/elephant-goldfish-model`), timeouts (`#424`), lint Python/workflows (`#427`) et bumps de dépendances (`#339`, `#362`, `#384`, `#440`).
   - **Exclure totalement** ce qui est couplé à l'organisation Google : `.github/CODEOWNERS` (`#340` -> conserver la version fork), `.gemini/**` (`#320`), `.github/workflows/pr-triage-review.yml`, `.github/scripts/review_pr.py`, `tests/unit/test_pr_triage_review.py` (`#380`/`#413`/`#439`) et `.github/workflows/scorecard.yml` (`#425`).

## Contrats et invariants à préserver

1. **Surface publique exacte des skills** (encodée dans [`tests/unit/test_adaptive_workflow.py`](../../tests/unit/test_adaptive_workflow.py)) :
   - `PUBLIC_SKILLS == {"egm-design", "egm-review", "egm-drift-report", "egm-bootstrap"}`.
   - `RETIRED` dans `tests/unit/test_adaptive_workflow.py` est étendu à `{"egm-brainstorm", "egm-draft", "egm-resolve", "egm-review-loop", "egm-lite"}` afin que les tests offline garantissent l'absence de `egm-lite` et de toute référence résiduelle dans `skills/**/*.md`, `agents/*.md` et `resources/**/*.md`.
   - Invocation explicite uniquement (`disable-model-invocation: true`, `allow_implicit_invocation: false`).
   - Aucune référence aux artefacts obligatoires supprimés (`concepts_brief.md`, `design_draft.md`, `zoom_out_report.md`, `goldfish_review_report.md`, `consolidated_review_report.md`).

2. **Contrat de livraison `Definition of Done`** (PR #3, [`docs/designs/definition_of_done.md`](definition_of_done.md)) :
   - `skills/egm-design/SKILL.md`, `skills/egm-design/references/design_doc.md`, `skills/egm-design/test_scenarios.yaml`, `skills/egm-design/TEST.md` et `tests/unit/test_adaptive_workflow.py` préservent intégralement les 3 portes de livraison (`Design approved`, `Implementation verified`, `PR delivered`) et les 6 scénarios `delivery_*`.

3. **Propriétaire unique de la revue, spécialiste TRIZ et adaptateurs** :
   - `egm-design` et `egm-review` partagent `resources/review-workflow.md` et `resources/execution_instructions.md`.
   - `agents/inventive_catalyst.md` (`name: egm-inventive-catalyst`) est strictement lecture seule, enregistré dans `.claude-plugin/agents/inventive_catalyst.md`, `.cursor-plugin/agents/inventive_catalyst.md`, `com.github.copilot/agents/egm-inventive-catalyst.agent.md` et `adapters/opencode/install.py` (ajout de `"inventive_catalyst"` à `REVIEWERS`), et documenté comme spécialiste optionnel dans `resources/review-workflow.md`.
   - Mises à jour contractuelles associées :
     - `scripts/pack_plugin.py` : ajouter `"agents/inventive_catalyst.md"` à `REQUIRED_SHARED` (et retirer toute référence Windsurf / `egm-lite`).
     - `tests/unit/test_harnesses.py` : ajouter `"inventive_catalyst"` à `REVIEWERS` (importé par `test_copilot_adapter.py` et `test_cursor.py`).
     - `tests/unit/test_opencode_adapter.py` : mettre à jour le décompte attendu des agents générés de `8` à `9` (8 reviewers + agent principal `egm`).
     - `tests/unit/test_packaging.py` : remplacer `test_published_claude_runtime_is_current` (qui comparait contre le répertoire supprimé `distributions/claude/`) par la vérification dynamique `#394` du runtime généré par `build(ROOT, "claude", tmp_path)` (présence de `NOTICE`, `skills/egm-design/`, `agents/inventive_catalyst.md`, absence de `egm-lite` et Windsurf).
     - `com.github.copilot/agents/egm.agent.md` et `docs/*.md` (`docs/codex.md`, `docs/harnesses.md`, `docs/muse.md`, `docs/copilot.md`, `docs/cursor.md`, `docs/opencode.md`, `docs/claude.md`, `docs/getting_started.md`) : aligner le nombre exact de profils reviewers et conserver `egm-design-critic`.
   - La protection des URLs externes dans `egm-review` (`#289` : sauvegarde des URLs `GoldfishContext` en fichiers temporaires après accord utilisateur) est portée sur `skills/egm-review/SKILL.md`, `TEST.md` et `test_scenarios.yaml` sans réintroduire `egm-review-loop`.

4. **Identité indépendante du fork et conformité Apache-2.0** :
   - [`NOTICE`](../../NOTICE) est conservé intégralement et inclus dans toutes les archives générées par `scripts/pack_plugin.py` (y compris le package Claude dérivé).
   - Tous les manifests (`plugin.json`, `.plugin/plugin.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.cursor-plugin/marketplace.json`, `.agents/plugins/marketplace.json`) déclarent `Acrazie` comme auteur/mainteneur, version `0.1.0` (pour les manifests versionnés), et pointent vers `https://github.com/Acrazie/elephant-goldfish-model`.
   - `scripts/prepare_release.py` pointe vers `Acrazie/elephant-goldfish-model` dans la commande d'attestation de `RELEASE_NOTES.md`.

5. **Validation des traces Codex** (combinaison exacte de PR #2 et upstream `#297`) :
   - Dans `tests/integration/test_codex.py` (`successful_reads`) :
     - Rejeter les sorties vides ou composées uniquement d'espaces : `not (item.get("aggregated_output") or "").strip()` (`#297`).
     - Résoudre `cwd` via `pathlib.Path(url2pathname(urlparse(cwd_value).path))` (`#297`, compatibilité chemins Windows `file:///C:/...`).
     - Préserver les règles de PR #2 : `type == "read"` exige `exit_code == 0`, et `type == "unknown"` (`cat`) exige la présence effective du contenu du fichier lu dans `aggregated_output` (tout en rejetant `&&`, pipes `|` et sorties d'erreur sans contenu).
   - `tests/unit/test_codex_traces.py` conserve et exécute l'ensemble des cas de régression de PR #2 et de `#297`.

6. **Cohérence du site documentaire (`site/` + `docs/site/`) et intégrité des liens** :
   - `docs/site/skills/` contient exactement les 4 pages de skills du fork (`egm-design.md`, `egm-review.md`, `egm-bootstrap.md`, `egm-drift-report.md`).
   - `docs/site/getting-started.md`, `guide.md`, `install.md`, `skills.md`, `workflow.md` décrivent le workflow adaptatif du fork et ses 4 commandes.
   - `site/src/lib/repository-markdown.mjs`, `site/src/lib/github-stars.ts`, `site/scripts/check-docs.mjs`, `site/astro.config.mjs` et `site/tests/*` pointent vers `Acrazie/elephant-goldfish-model` et `skills/egm-design/SKILL.md` (aucune fixture morte vers `egm-draft` ou `egm-lite`).
   - `docs/designs/triz_integration.md` (adopté depuis `#290`) a ses liens relatifs vers des skills retirés (`egm-brainstorm`, `egm-draft`, `egm-review-loop`) adaptés (comme dans `docs/designs/README.md`) afin que `tests/unit/test_link_integrity.py` passe.

## Ordre d'exécution sûr (pour l'implémentation)

L'exécution du merge suit cet ordre pour éviter les ajouts exclus silencieux et isoler les conflits :

1. **Pré-vol** : vérifier que l'arbre de travail est propre sur `main` (`fcb2b62`), créer la branche `sync/upstream-70406c4` et fetcher `70406c4` depuis `https://github.com/google/elephant-goldfish-model.git`.
2. **Merge sans commit** : exécuter `git merge --no-commit --no-ff 70406c4`.
3. **Purge immédiate des zones exclues et retirées** (y compris les fichiers ajoutés sans conflit par upstream) :
   - `git rm -rf --ignore-unmatch distributions/claude .windsurf skills/egm-lite skills/egm-brainstorm skills/egm-draft skills/egm-resolve skills/egm-review-loop .gemini .github/workflows/pr-triage-review.yml .github/scripts/review_pr.py tests/unit/test_pr_triage_review.py .github/workflows/scorecard.yml docs/designs/lite.md docs/designs/windsurf_support.md tests/unit/test_windsurf.py docs/site/skills/egm-brainstorm.md docs/site/skills/egm-draft.md docs/site/skills/egm-resolve.md docs/site/skills/egm-review-loop.md docs/site/skills/egm-lite.md`
   - Restaurer `.github/CODEOWNERS` depuis `HEAD` (`fcb2b62`).
4. **Résolution du cœur runtime, packaging, adaptateurs et tests Python** :
   - Résoudre `skills/egm-review/**`, `skills/egm-bootstrap/**`, `resources/review-workflow.md`, `agents/**`, `.claude-plugin/**`, `.cursor-plugin/**`, `.codex-plugin/**`, `.plugin/**`, `.agents/plugins/marketplace.json`, `plugin.json`, `com.github.copilot/**`, `adapters/opencode/install.py`, `scripts/pack_plugin.py`, `scripts/prepare_release.py`, `docs/*.md`, `docs/designs/**`, `tests/integration/test_codex.py` et `tests/unit/**`.
   - Exécuter `pytest tests/unit` et un dry-run de `scripts/pack_plugin.py` comme point de contrôle intermédiaire avant d'attaquer `site/`.
5. **Adaptation de `site/` et `docs/site/`** :
   - Créer `docs/site/skills/egm-design.md`, réécrire les pages `docs/site/*.md` pour le fork, mettre à jour les URLs/fixtures `site/` vers `Acrazie/elephant-goldfish-model` et `skills/egm-design/SKILL.md`.
   - Exécuter la séquence complète de validation Astro (`npm ci`, `npm test`, `npm run check`, builds avec/sans analytics, `npm run test:browser`).
6. **Workflows CI, docs racine et vérification finale** :
   - Résoudre `.github/workflows/*.yml`, `pyproject.toml`, `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, `AI_POLICY.md`, `TESTING.md`, `.github/PULL_REQUEST_TEMPLATE.md`.
   - Relancer la totalité des vérifications de la `Definition of Done` après les dernières éditions avant de valider le merge commit local (sans push ni PR avant validation humaine).

## Périmètre d'écriture autorisé et matrice de résolution

Sous mandat d'implémentation séparé après approbation humaine, les opérations suivantes sont autorisées sur la branche `sync/upstream-70406c4` :

- **Règle générale pour les fichiers sans conflit hors zones exclues** : les ajouts/modifications upstream propres (ex. assets du nouveau site, mises à jour mineures de docs/dépendances hors périmètre exclu) sont conservés tels quels par le merge.
- **Create** : `agents/inventive_catalyst.md`, `.claude-plugin/agents/inventive_catalyst.md`, `.cursor-plugin/agents/inventive_catalyst.md`, `.cursor-plugin/marketplace.json`, `com.github.copilot/agents/egm-inventive-catalyst.agent.md`, `docs/designs/triz_integration.md`, `docs/site/**` (adapté au fork, incluant `docs/site/skills/egm-design.md`), nouveaux composants/scripts/assets `site/**` issus de la refonte upstream.
- **Delete** : `distributions/claude/**`, `.windsurf/**`, `skills/egm-lite/**`, `skills/egm-brainstorm/**`, `skills/egm-draft/**`, `skills/egm-resolve/**`, `skills/egm-review-loop/**`, `.gemini/**`, `.github/workflows/pr-triage-review.yml`, `.github/scripts/review_pr.py`, `tests/unit/test_pr_triage_review.py`, `.github/workflows/scorecard.yml`, `docs/designs/lite.md`, `docs/designs/windsurf_support.md`, `tests/unit/test_windsurf.py`, `docs/site/skills/{egm-brainstorm,egm-draft,egm-resolve,egm-review-loop,egm-lite}.md`, composants `site/` supprimés par la refonte upstream (`Hero.astro`, `Install.astro`, `Loop.astro`, `Model.astro`, `Skills.astro`).
- **Modify** :
  - *Skills & ressources* : `skills/egm-review/**`, `skills/egm-bootstrap/**`, `skills/egm-drift-report/**` (si touché), `resources/review-workflow.md`, `resources/execution_instructions.md` (préservé), `agents/*.md` (`synthesizer.md`, etc.).
  - *Manifests & adaptateurs* : `plugin.json`, `.plugin/plugin.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `com.github.copilot/agents/egm.agent.md`, `adapters/opencode/install.py`, `assets/**`.
  - *Scripts* : `scripts/pack_plugin.py`, `scripts/prepare_release.py`.
  - *Tests* : `tests/integration/test_codex.py`, `tests/unit/test_codex_traces.py`, `tests/unit/test_adaptive_workflow.py`, `tests/unit/test_packaging.py`, `tests/unit/test_harnesses.py`, `tests/unit/test_frontmatter.py`, `tests/unit/test_copilot_adapter.py`, `tests/unit/test_cursor.py`, `tests/unit/test_opencode_adapter.py`, `tests/unit/test_link_integrity.py`.
  - *Documentation* : `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, `AI_POLICY.md`, `TESTING.md`, `docs/*.md` (`claude.md`, `codex.md`, `harnesses.md`, `muse.md`, `copilot.md`, `cursor.md`, `opencode.md`, `getting_started.md`, `directory.md`, `releases.md`), `docs/designs/README.md` et designs existants touchés (en préservant les notes historiques du fork et `definition_of_done.md`).
  - *Site & CI* : `site/**`, `.github/workflows/tests.yml`, `.github/workflows/deploy-site.yml`, `.github/workflows/release.yml`, `.github/workflows/pr-scope-advisory.yml`, `.github/workflows/*-native.yml`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/**`, `pyproject.toml`.

## Risques et retour arrière (Rollback)

- **Régression dans `scripts/pack_plugin.py` après suppression de `distributions/claude/`** : atténuée par le remplacement de `test_published_claude_runtime_is_current`, l'ajout de `agents/inventive_catalyst.md` dans `REQUIRED_SHARED` et un dry-run complet du packaging.
- **Fuite d'identité Google ou de skills retirés/exclus dans `site/` et `docs/`** : atténuée par l'extension de `RETIRED` dans `test_adaptive_workflow.py`, un audit grep dédié sur `docs/site/`, `site/src/` et les manifests, ainsi que `test_link_integrity.py`.
- **Plan de retour arrière** : la synchronisation s'exécute exclusivement sur `sync/upstream-70406c4` sans modifier `main`. Avant commit, `git merge --abort` restaure l'état initial ; après commit local, la suppression de la branche `sync/upstream-70406c4` laisse `main` intact sur `fcb2b62`.

## Definition of Done

Pour l'implémentation de cette synchronisation :

- **Merge Git propre** : `git merge-base --is-ancestor 70406c4 HEAD` retourne `0` et `git merge-base --is-ancestor fcb2b62 HEAD` retourne `0` sur `sync/upstream-70406c4`, sans réécriture de `main` ni marqueurs de conflit résiduels (`git diff --check` passe).
- **Tests unitaires offline** : `python -m pytest tests/unit` passe sans échec (tout skip optionnel documenté, ex. probes Copilot/Cursor locaux), couvrant `test_adaptive_workflow.py` (incluant `egm-lite` dans `RETIRED`), `test_codex_traces.py` (cas PR #2 + `#297`), `test_packaging.py` (vérification dynamique Claude `#394`), `test_harnesses.py`, `test_frontmatter.py`, `test_copilot_adapter.py`, `test_cursor.py`, `test_opencode_adapter.py` (9 agents) et `test_link_integrity.py` (incluant `docs/designs/triz_integration.md`).
- **Exclusions vérifiées** : absence confirmée dans l'arbre de travail de `distributions/claude/`, `.windsurf/`, `skills/egm-lite/`, `skills/egm-brainstorm/`, `skills/egm-draft/`, `skills/egm-resolve/`, `skills/egm-review-loop/`, `.gemini/`, `.github/workflows/pr-triage-review.yml`, `.github/scripts/review_pr.py`, `tests/unit/test_pr_triage_review.py`, `.github/workflows/scorecard.yml`, `docs/designs/lite.md`, `docs/designs/windsurf_support.md`, `tests/unit/test_windsurf.py`, `docs/site/skills/{egm-brainstorm,egm-draft,egm-resolve,egm-review-loop,egm-lite}.md` ; version `0.1.0` uniforme et auteur `Acrazie` (jamais `Google LLC`) dans les manifests du fork ; absence de `@google/egm-maintainers` dans `.github/CODEOWNERS`.
- **Intégration TRIZ vérifiée** : `agents/inventive_catalyst.md` (`egm-inventive-catalyst`) est présent, enregistré sur Claude, Cursor, Copilot et OpenCode, ajouté à `REQUIRED_SHARED` dans `scripts/pack_plugin.py`, documenté comme spécialiste optionnel dans `resources/review-workflow.md` et couvert par les tests d'adaptateurs/frontmatter.
- **Packaging vérifié** : exécution réelle de `scripts/pack_plugin.py` confirmant la génération des archives (dont le runtime Claude sans `distributions/claude/` commité), avec `NOTICE`, `skills/egm-design/` et `agents/inventive_catalyst.md` présents et sans `egm-lite` ni Windsurf.
- **Site Astro vérifié** : dans `site/`, exécution exacte de la séquence `.github/workflows/tests.yml` (`npm ci`, `npm test`, `npm run check`, `PUBLIC_GA_MEASUREMENT_ID='' npm run build` suivi de la copie de `dist/index.html` vers un fichier temporaire, `PUBLIC_GA_MEASUREMENT_ID=G-TEST npm run build`, puis `npm run test:browser -- "<fichier-temp-without-analytics>"`) — tous passent ; audit grep confirmant l'absence de références mortes aux skills retirés/exclus ou au dépôt `google/elephant-goldfish-model` dans `docs/site/` et `site/src/` (hors attribution `NOTICE`/licence).
- **Linters CI (`#427`)** : exécution des linters Python et workflows ajoutés par `#427` après les dernières modifications. Ce check est **bloquant pour la porte 2 (`Implémentation vérifiée`)** : si les binaires requis ne sont pas disponibles localement, la porte 2 ne peut pas être déclarée atteinte tant que ces linters n'ont pas été exécutés et validés (localement ou via CI).
- **Limite de vérification comportementale native (non bloquante pour ce sync offline)** : l'exécution native sur modèles LLM pour `egm-inventive-catalyst` et `egm-review` (`#289`) est **hors périmètre de la validation offline** faute de quota/harnesses installés ; elle ne bloque pas la porte 2 mais doit être explicitement consignée comme limite de vérification (non exécutée) dans le rapport de livraison.

### Portes de livraison séparées

1. **Design approuvé** : la présente révision de `docs/designs/upstream_sync.md` a complété sa revue indépendante (`egm-design-critic` + `egm-implementation-readiness`), résolu ses points bloquants/majeurs et reçu l'approbation explicite de l'humain. Cette porte n'autorise ni l'implémentation ni la publication.
2. **Implémentation vérifiée** : sous mandat séparé, tous les critères bloquants ci-dessus sont satisfaits dans le périmètre autorisé après les dernières modifications, avec enregistrement du commit/digest vérifié, des commandes exécutées, des résultats observés et des limites explicites (dont l'absence de runs LLM natifs). Tout échec ou check bloquant non exécuté empêche cette porte.
3. **PR livrée** : après revue humaine du diff réel, des preuves de vérification et approbation explicite de publication, ouverture/mise à jour de la PR selon `.github/PULL_REQUEST_TEMPLATE.md` (case *Accountability* cochée par l'humain), avec URL de PR, SHA de tête et statut des checks CI distants (aucun check requis en échec ou en attente).

## Métadonnées de revue et d'approbation

Digest domain: UTF-8 bytes before the `## Métadonnées de revue et d'approbation` heading.
Reviewed body SHA-256: `b0576ad44820625c91e74ff1dfe65fbdc789186c3bda90cffa218630a0324870`.
Selected source baseline: local `main` HEAD `fcb2b62657a3c3b10f1cf8635569d90df1a5d17f` (fork) et cible upstream `google/elephant-goldfish-model@70406c4`.
Couverture complétée (revue initiale sur `9d8d5548...` suivie d'une revalidation ciblée en contexte frais sur `b0576ad4...`) :
- `egm-design-critic` : 0 Blocker, 0 Major, 1 Nit non bloquant (chemin exact du manifest Copilot `#311` implicite dans `com.github.copilot/**`).
- `egm-implementation-readiness` : 0 Blocker, 0 Major, 1 Nit non bloquant (au point de contrôle intermédiaire étape 4, `test_link_integrity.py` peut signaler des liens `docs/site/` avant l'étape 5 ; la passe finale étape 6 reste complète).
Décisions humaines enregistrées : merge commit unique `70406c4` dans `sync/upstream-70406c4` ; intégration de `egm-inventive-catalyst` (TRIZ `#299`) uniquement (Windsurf `#379` et `egm-lite` `#438` exclus) ; suppression de `distributions/claude/` (`#393`/`#394`) et adoption/adaptation de `site/` ; CI générique retenue (`#341`, `#424`, `#426`, `#427`) et gouvernance Google exclue (`CODEOWNERS`, `.gemini/`, `pr-triage-review.yml`, `scorecard.yml`).
Point à confirmer à l'approbation humaine : maintien de la version fork `0.1.0` (vs bump upstream `0.1.1`) et conservation de `.cursor-plugin/marketplace.json` adapté au fork.
Limites d'évidence : revues en lecture seule sans exécution de tests/linters ni inspection directe des objets Git locaux de `70406c4` par les reviewers (le diff upstream a été inspecté via `gh api` par l'agent principal) ; l'isolation de contexte frais ne prouve pas l'exclusion des fichiers d'instructions de l'hôte.
Statut : approuvé par l'humain le 2026-11-20 pour le digest `b0576ad44820625c91e74ff1dfe65fbdc789186c3bda90cffa218630a0324870` ; mandat d'implémentation séparé accordé le 2026-11-20 (sans push ni PR avant validation humaine de l'implémentation).
