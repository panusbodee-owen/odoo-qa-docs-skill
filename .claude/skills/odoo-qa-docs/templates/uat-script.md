# Template: UAT Script + Sign-off

UAT = business end-to-end scenarios run by key users with real-like data. Fewer, longer scenarios than SIT (usually 5–10 per module). Write for non-technical users.

## Output format

```
# UAT Script — <Module/Process> — <Project>
| Version | Odoo <ver> | UAT Round | 1 | Environment | UAT DB `<name>` | Period | <dates> |
|---|---|---|---|---|---|---|---|

## Scenario List
| Scenario ID | Business Scenario | Key User | Related TC | Priority |
|---|---|---|---|---|
| UAT-SO-01 | Credit sale: deliver, issue tax invoice, receive payment | <name/role> | TC-SO-001..005 | High |

## UAT-SO-01 : <Business Scenario>
Objective: <1 line> | Precondition: <1 line> | Test Data: <1 line>

| Step | Role | Action (Menu > Button) | Expected Result | Actual Result | Pass/Fail | Evidence |
|---|---|---|---|---|---|---|
| 1 | Sales | Sales > Orders > Quotations > **New** ... **Confirm** | SO state = Sales Order | | | |
| 2 | Warehouse | Inventory > Operations > Deliveries > open DO > **Validate** | DO = Done, stock decreases by 2 | | | |
| 3 | Account | SO > **Create Invoice** > **Confirm** | Invoice Posted, JE: Dr AR / Cr Revenue, Output VAT | | | |
```

## Sign-off section (always last)
```
## Issue Summary
| Issue ID | Scenario | Severity | Description | Status |
|---|---|---|---|---|

## UAT Sign-off
| Result | ☐ Accepted ☐ Accepted with conditions ☐ Rejected |
|---|---|
| Conditions | |

| Role | Name | Signature | Date |
|---|---|---|---|
| Key User | | | |
| Process Owner | | | |
| Project Manager (Customer) | | | |
| Project Manager (Implementer) | | | |
```
