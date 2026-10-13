# Template: Upgrade Regression Test (vOLD → vNEW)

Load `versions/vNEW.md` (and `versions/vOLD.md` if it exists). Focus on what an upgrade breaks; do not retest unchanged standard flows in depth.

## Coverage order
1. Data migration integrity: counts & totals equal before/after (partners, products, open SO/PO, stock on hand & valuation, AR/AP balance, trial balance).
2. Open documents continue: draft/confirmed SO/PO/MO/transfers can be finished in vNEW.
3. Every delta row between vOLD and vNEW (rows in `versions/vOLD.md` and/or `versions/vNEW.md`; v18 is the baseline with no rows) → at least one TC.
4. Custom modules / Studio fields / reports / automated actions / server actions.
5. Integrations (API, EDI, bank files, e-Tax) and scheduled actions.
6. Permissions & record rules per role.

## Output format
```
# Upgrade Regression — Odoo <OLD> → <NEW> — <Project>
| Old DB | | New DB | | Cut-off date | | Prepared by | |
|---|---|---|---|---|---|---|---|

## Data Reconciliation
| Check ID | Object | Measure | vOLD value | vNEW value | Match | Remark |
|---|---|---|---|---|---|---|
| DR-01 | Trial Balance | Total Dr/Cr at cut-off | | | | |
| DR-02 | Stock | Qty on hand + valuation per warehouse | | | | |

## Regression Test Cases
| TC ID | Area | Change Ref | Steps | Expected Result | Priority | Status | Remark |
|---|---|---|---|---|---|---|---|
| RG-INV-001 | Product type | v17.md: Product type | ... | ... | High | Not Run | |
```
TC ID: `RG-<MOD>-<NNN>`. Change Ref = version-file row or custom module name.
