---
name: odoo-dev
description: Odoo developer assistant for custom modules, any version (16, 17, 18, 19, 20+) — scaffolds modules, writes models/views/security/wizards/QWeb reports/controllers/OWL, writes tests, migrates code between versions, reviews modules for deprecated patterns, Thai localization (baht text, Thai PDF fonts, Tax ID). Use when the user asks to create, customize, fix, review, upgrade or port an Odoo module, addon, field, view, report, cron, API endpoint, or Python/XML/JS code for Odoo.
---

# Odoo Dev (version-aware, token-efficient)

## Token rules (always follow)
1. Load only what the task needs: `references/versions.md` (always, once) + at most one other reference.
2. New module → run `scripts/scaffold.py`, never hand-write boilerplate. Review/upgrade → run `scripts/check_compat.py` first and fix only what it reports + what the user asked.
3. Show diffs/edited blocks only, never reprint whole unchanged files. No explanations of standard Odoo concepts unless asked.
4. Read existing code with Grep/targeted reads; do not read all of `odoo/addons` — inherit by XML id / model name you already know, verify with one grep if unsure.
5. Ask at most one question (target version / edition) only if it cannot be inferred from `__manifest__.py` `version`, the user, or the repo branch name.

## Step 1 — Target version
Infer from manifest `version` (`18.0.x.y.z` → 18), branch name, or user. Default 18. Apply every rule for that version in `references/versions.md`. Unknown/future version: use the latest known rules + tag unverified API names `(verify)`; append confirmed changes to `versions.md` afterwards.

## Step 2 — Pick the reference
| Task | Load |
|---|---|
| Models, fields, compute, constraints, inheritance, security, wizard, cron, report, controller | `references/patterns.md` |
| Unit tests, tours, running tests, debugging | `references/testing.md` |
| Thai requirements (baht text, Buddhist year, Thai font PDF, Tax ID/branch, WHT) | `references/l10n-th.md` |

## Scripts (run, do not read)
```bash
S=.claude/skills/odoo-dev/scripts   # or ~/.claude/skills/odoo-dev/scripts
python3 $S/scaffold.py <module_name> --version 18 [--model x.model] [--depends sale,stock] [--path addons]
python3 $S/check_compat.py <module_path> --version 18      # prints file:line  RULE  hint
```

## Coding standard (all versions)
- OCA/Odoo guidelines: one model per file, `models/`, `views/`, `security/`, `data/`, `wizard/`, `report/`, `tests/`; XML ids `view_<model>_<type>`, `action_<model>`, `menu_<...>`.
- Never `cr.commit()` in business code; no raw SQL unless needed for performance (then `self.env.cr.execute` with params, `flush_model()` before, `invalidate_model()` after).
- Batch-safe: loop `for rec in self`, `@api.model_create_multi` for `create`, avoid search inside loops (prefetch / `read_group`).
- Every new model ⇒ `ir.model.access.csv` line(s); multi-company ⇒ `company_id` + record rule + `check_company=True`.
- Translations: user-facing strings with `_()` (v18+: `self.env._()` also available (verify)); pass values as `_("Text %s", value)`, never f-strings inside `_()`.
- Bump manifest `version` when data/model changes; add `migrations/<ver>/pre|post-migrate.py` if existing data must be transformed.
- Customer changes go in custom modules, never edit core or OCA code in place.

## Output
Code blocks with file path as heading. After code: install/upgrade command and a ≤3-line test hint, e.g. `odoo-bin -d db -u my_module --test-enable --test-tags /my_module --stop-after-init`.
