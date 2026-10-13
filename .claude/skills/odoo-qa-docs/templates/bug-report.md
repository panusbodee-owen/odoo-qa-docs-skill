# Template: Bug / Defect Report

Input is often a tester's messy note or screenshot. Convert to this exact format, nothing else. One report per bug.

```
**[BUG-<MOD>-<NNN>] <Short title: what is wrong, where>**
| Field | Value |
|---|---|
| Module / Menu | Sales > Orders > Quotations |
| Environment | <UAT/SIT DB>, Odoo <ver> <CE/EE>, browser |
| Severity | Critical / Major / Minor / Trivial |
| Priority | P1 / P2 / P3 |
| Related TC | TC-SO-003 |
| Reporter / Date | |

**Steps to Reproduce**
1. ...
2. ...

**Expected:** ...
**Actual:** ... (error message verbatim)
**Evidence:** <screenshot/video/log>
**Suspected Cause (optional):** config / data / custom module / standard bug
```

Severity guide:
- Critical: blocks process, data wrong in accounting/stock, no workaround.
- Major: process works with workaround, or wrong result in non-financial data.
- Minor: UI/label/report layout, easy workaround.
- Trivial: typo, cosmetic.

If the cause is likely configuration (not a bug), say so in one line under Suspected Cause and suggest the setting to check.
