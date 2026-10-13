---
name: odoo-qa-docs
description: Odoo QA & documentation for Thai implementation projects, any version (16, 17, 18, 19, 20+) — writes Test Cases, UAT scripts, User Manuals, Bug Reports and upgrade regression tests, exports to Excel/Word. Use when the user asks for test case, UAT, SIT, regression, upgrade test, user manual, SOP, work instruction, bug report, defect, or QA for an Odoo module/process (Sales, Purchase, Inventory, Accounting, MRP, POS, CRM).
---

# Odoo QA & Docs (Thailand, version-aware)

## Token rules (always follow)
1. Load ONLY the files needed: one template + one version file + only the module file(s) in scope. Never load all.
2. Do not echo the user's input, do not explain the template, no preamble. Output the deliverable directly.
3. Ask at most ONE round of questions, only if module/process/version is unknown. Otherwise assume defaults below and list assumptions in ≤3 bullets at the end.
4. Use tables, not prose. One line per step. No repeated text across rows — put shared preconditions/data once in a header block.
5. Large requests (>30 test cases or >1 module): write straight to a file in batches per module; reply with path + counts only, not the content.
6. Exports go through `scripts/export.py` (run it, do not read it).

## Defaults (unless user says otherwise)
- Version: as stated by user / project spec; if not stated → Odoo 18. Community/Enterprise per user.
- Company in Thailand, currency THB, VAT 7%.
- Document language: Thai (switch to English or other if the user asks). Template labels are written in English — render them in the document language. Odoo menu/button/field names in English exactly as in the target version UI (e.g. `Sales > Orders > Quotations`, button **Confirm**).
- Output folder: `docs/<type>/` in the working project. File name: `<TYPE>_<MODULE>_v<ver>_<yyyymmdd>.md`.

## Step 1 — Version → load `versions/v<ver>.md`
- `modules/*.md` = v18 baseline. The version file lists only deltas; deltas override the baseline.
- Version file missing, or Status PARTIAL → follow `versions/_new-version.md` (tag unconfirmed UI names `(verify)`, record confirmed deltas so the next run is cheap).

## Step 2 — Mode → load that template
| User asks for | Template | Typical export |
|---|---|---|
| Test case / SIT | `templates/test-case.md` | xlsx |
| UAT script / sign-off | `templates/uat-script.md` | xlsx + docx |
| Upgrade / regression test (vOLD→vNEW) | `templates/upgrade-regression.md` | xlsx |
| User manual / SOP | `templates/user-manual.md` | docx |
| Bug / defect report | `templates/bug-report.md` | md (paste to tracker) |

## Step 3 — Module knowledge → load only what is in scope
`modules/sales.md`, `modules/purchase.md`, `modules/inventory.md`, `modules/accounting-th.md`, `modules/mrp.md`, `modules/pos.md`, `modules/crm.md`.
Module not listed → use your own Odoo knowledge for that version and mark uncertain menu paths `(verify)`.

## Accuracy
- Never invent customer-specific config. Customizations / Studio fields from the user's spec (FSD, BRD, Fit-Gap) take priority over standard behavior.
- If an Odoo MCP/agent connection is available and the user asks to verify, check menu/field names against the live instance instead of guessing.
- Mark anything that depends on configuration as `[CONFIG]` in the Remark column.

## Export
```bash
python3 .claude/skills/odoo-qa-docs/scripts/export.py <file.md> [--xlsx] [--docx]
```
- `--xlsx`: every Markdown table → one sheet (styled header, wrap text, Thai font, freeze header, Status dropdown).
- `--docx`: whole Markdown → Word via pandoc (headings, tables, image placeholders kept).
Default with no flag: both.
