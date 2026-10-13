# Template: User Manual / SOP

Audience: end users. Short sentences, imperative ("Click **Confirm**"). One process per chapter. No theory — only what the user clicks and checks. Labels below are in English; render them in the document language (default Thai).

## Output format

```
# User Manual — Odoo <ver> — <Module>
| Project | <name> | Document version | 1.0 | Date | <yyyy-mm-dd> | Prepared by | |
|---|---|---|---|---|---|---|---|

## Table of Contents
1. <Process 1>
2. <Process 2>

## 1. <Process name>
**Purpose:** <1 line>
**Users / Access rights:** <role> (<Odoo group>)
**Menu:** `Sales > Orders > Quotations`
**Before you start:** <required master data / settings>

### Steps
| # | Action | Note |
|---|---|---|
| 1 | Go to `Sales > Orders > Quotations`, click **New** | ![Figure 1.1](images/1-1.png) |
| 2 | Enter **Customer** | Required field |
| 3 | In tab **Order Lines** click **Add a product**, select product, enter **Quantity** | Price comes from the Pricelist automatically |
| 4 | Click **Confirm** | State changes to Sales Order |

### Result check
- <state / document created / figures to verify>

### Cautions / FAQ
- **Q:** ... **A:** ...
```

## Rules
- Screenshot placeholders: `![Figure <chapter>.<n>](images/<chapter>-<n>.png)` — only where the screen changes, max 1 per 2 steps.
- Field/button names exactly as the target version UI (English) — explanation in the document language in the Note column if needed.
- Customer-specific fields (Studio/custom module): mark `(Custom)`.
- End chapter with result-check list; end document with a glossary only if user asks.
