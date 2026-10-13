# Template: Test Case (SIT / Functional)

## Coverage rule
Per process cover, in this order: Happy path → Negative (validation/permission) → Boundary (qty 0, decimals, rounding, max) → Integration (downstream doc created: invoice, stock move, journal entry). Default 8–15 TC per process; more only if user asks.

## ID convention
`TC-<MOD>-<NNN>` — MOD: SO, PO, INV, ACC, MRP, POS, CRM. Number by step of 1, grouped by scenario.

## Output format (Markdown, exportable)

```
# Test Case — <Module> — <Process>
| Project | <name> | Version | Odoo <ver> <CE/EE> | Prepared by | | Date | <yyyy-mm-dd> |
|---|---|---|---|---|---|---|---|

## Shared Preconditions
- PRE-1: User `<role>` has group `<Sales / User: All Documents>` ...
- PRE-2: Master data: Customer `C001`, Product `P001` (Goods + Track Inventory, price 1,000, VAT 7%)

## Test Cases
| TC ID | Scenario | Type | Pre | Steps | Test Data | Expected Result | Priority | Status | Remark |
|---|---|---|---|---|---|---|---|---|---|
| TC-SO-001 | Create and confirm quotation | Positive | PRE-1,2 | 1. Sales > Orders > Quotations > **New**<br>2. Select Customer, add Product<br>3. **Confirm** | C001, P001 x 2 | State = Sales Order, 1 Delivery created, Untaxed 2,000 / Tax 140 / Total 2,140 | High | Not Run | |
```

Column rules:
- Type: Positive | Negative | Boundary | Integration | Permission
- Priority: High (blocks go-live) | Medium | Low
- Status (leave for tester): Not Run | Pass | Fail | Blocked | N/A
- Steps: numbered, `<br>` between steps, menu path in English, buttons in **bold**.
- Expected Result: measurable (state, amount, qty, document created, error message). Never "works correctly".
- Remark: `[CONFIG]` if depends on settings; link to requirement ID if user gave one (e.g. `REQ-012`).

## End of file
`## Summary` table: Type × count, Priority × count. Then ≤3 assumption bullets.
