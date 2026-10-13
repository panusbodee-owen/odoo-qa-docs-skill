# Claude Skills for Odoo — QA, Documentation & Development (all versions)

This repository contains two skills: `odoo-qa-docs` (QA & documents) and `odoo-dev` (development).

## Skill 1 — `odoo-qa-docs` (QA & documentation)

The `odoo-qa-docs` skill helps testers, functional consultants and project managers on Odoo implementation projects in Thailand. It supports Odoo 16–19 and future versions (20+).

| Task | Output | Export |
|---|---|---|
| Test Case (SIT) | Test case table covering Positive / Negative / Boundary / Integration / Permission | Excel (with Status dropdown) |
| UAT Script | Business scenarios, result-recording table and sign-off page | Excel + Word |
| User Manual / SOP | Step-by-step instructions, menu paths, screenshot placeholders, FAQ | Word (Thai font TH Sarabun New) |
| Bug Report | Turns a tester's rough note into a standard defect report | Markdown |
| Upgrade Regression | Before/after data reconciliation + test cases for every version change | Excel |

## Skill 2 — `odoo-dev` (Odoo developer)

Helps developers build and maintain custom Odoo modules for versions 16–19 and future releases.

| Task | How |
|---|---|
| New module | `scripts/scaffold.py` generates a version-correct skeleton: model, list/form views, action, menu, access rights and a unit test |
| Upgrade / port / review | `scripts/check_compat.py` lists deprecated patterns for the target version (`attrs`, `<tree>`, `name_get`, `oe_chatter`, `group_operator`, `detailed_type`, …) with file:line |
| Models, views, security, wizards, cron, QWeb reports, controllers | `references/patterns.md` |
| Tests and debugging | `references/testing.md` (TransactionCase, Form, tours, odoo-bin commands) |
| Thai requirements | `references/l10n-th.md` (baht text, Buddhist year, Thai PDF fonts, Tax ID checksum, branch, WHT) |
| Version differences | `references/versions.md` — one table of rules; unknown future versions get `(verify)` tags until confirmed |

```bash
python3 .claude/skills/odoo-dev/scripts/scaffold.py my_request --version 18 --model x.request --depends base,mail --path addons
python3 .claude/skills/odoo-dev/scripts/check_compat.py addons/my_module --version 18
```

Example prompts:
- `Create a module for purchase requests with two-step approval, Odoo 18`
- `Port addons/my_module from 16 to 18`
- `Add a Thai tax invoice PDF with baht text and Buddhist year`
- `Write unit tests for TC-SO-001..005` (links QA test cases from `odoo-qa-docs` to automated tests)

## Structure (odoo-qa-docs)
```
.claude/skills/odoo-qa-docs/
├── SKILL.md            # core rules + mode router (kept as short as possible)
├── templates/          # loaded only for the mode in use
├── modules/            # per-module knowledge (baseline = v18): sales, purchase, inventory, accounting-th, mrp, pos, crm
├── versions/           # only the differences per version: v17, v18, v19, _new-version.md
└── scripts/export.py   # md → xlsx/docx (Claude runs it, never reads the code)
docs/examples/          # sample output
```

## Installation

### Option 1 — claude.ai / Claude Desktop
1. Download `odoo-qa-docs.zip` (or zip the folder `.claude/skills/odoo-qa-docs` yourself; the zip must contain the `odoo-qa-docs/` folder with `SKILL.md` inside).
2. Go to **Settings → Capabilities** and turn on **Code execution and file creation**.
3. In **Skills**, click **Upload skill** and select the zip. Enable `odoo-qa-docs`.

Menu names in claude.ai may change over time; look for the Skills section under Settings.

### Option 2 — Claude Code, for all projects
```bash
git clone https://github.com/panusbodee-owen/odoo-qa-docs-skill.git
mkdir -p ~/.claude/skills
cp -r odoo-qa-docs-skill/.claude/skills/odoo-qa-docs odoo-qa-docs-skill/.claude/skills/odoo-dev ~/.claude/skills/
```
Windows: copy the folder to `C:\Users\<username>\.claude\skills\`.
For a single project, place it in that project's `.claude/skills/` instead.

Export requirements: `pip install openpyxl python-docx`, plus [pandoc](https://pandoc.org) for Word output.

### Option 3 — whole team
Clone this repository; everyone who opens Claude Code in this repository gets the skill automatically.

### Check that it works
Ask: `Create 5 test cases for Sales quotation → invoice`. A table with IDs like `TC-SO-001` means the skill is active.

## Usage
Just ask in normal language, for example:
- `Create test cases for Sales: quotation → delivery → invoice with delivered-quantity policy, export to Excel`
- `Create a regression test for upgrading Odoo 17 → 18, Inventory module`
- `Create a UAT script for Purchase two-step approval with a 50,000 THB limit`
- `Write a user manual for receiving goods and stock counting for warehouse users`
- `Turn this into a bug report: validating the DO shows "lot required" even though the lot was entered`

You can attach a BRD / FSD / Fit-Gap. The skill always gives customer requirements priority over standard Odoo behavior.

Output documents are in Thai by default; ask for English (or another language) and the skill switches. Odoo menu, button and field names always stay in English, exactly as in the UI.

## Future Odoo versions
- `modules/` is written once as the v18 baseline. `versions/vNN.md` holds **only what differs** from the baseline, so less is loaded and each change lives in one place.
- For a new version without a file (e.g. v20) the skill: continues with the v18 baseline → tags every unconfirmed menu/button/field name `(verify)` → verifies against screenshots, release notes or a live instance → records confirmed differences in `versions/v20.md`, so later runs need no re-checking.
- When the company moves to a new version as its main one, that version can be promoted to the new baseline (see `versions/_new-version.md`).
- `v19.md` is currently PARTIAL — not yet confirmed against a live v19 instance.

## Why it saves tokens
1. **Progressive loading** — Claude only sees the skill name and description until the skill is used, then loads just one template, one version file and the relevant module files.
2. **Instructions are in English** — Thai text costs several times more tokens; output can still be in Thai.
3. **No preamble, no restating the request** — answers are tables; shared preconditions and test data are written once.
4. **Large jobs are written to files** — Claude replies with the file path and counts instead of repeating the content in chat.
5. **Export by script** — Claude does not build Excel/Word files itself.

## Customization
- Add a module: create `modules/<name>.md` in the same format (menus, flow, settings, checklist) and list it in `SKILL.md`.
- Change the Word layout: edit `scripts/reference.docx` (styles, fonts, header logo).
- Add project conventions (TC naming, customer roles) to the Defaults section of `SKILL.md`.
