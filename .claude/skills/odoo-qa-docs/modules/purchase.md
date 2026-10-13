# Purchase (baseline: Odoo 18 — apply `versions/vNN.md` deltas for other versions)

Menus: `Purchase > Orders > Requests for Quotation | Purchase Orders` · `Purchase > Orders > Vendors` · `Purchase > Products > Products` · `Purchase > Configuration > Settings` · Agreements `Purchase > Orders > Purchase Agreements` [CONFIG]
Flow: RFQ → **Send by Email** → **Confirm Order** (PO) → **Receive Products** → Validate receipt → **Create Bill** → Bill **Confirm** → **Register Payment**
States: RFQ → RFQ Sent → To Approve → Purchase Order → Locked / Cancelled

Settings [CONFIG]: Purchase Order Approval (two-step, min amount), Lock Confirmed Orders, Warnings, Purchase Agreements (Blanket Order / Call for Tenders), Vendor pricelists, Receipt Reminder, Variants, UoM.
Product: Control Policy (Bill on) = Ordered quantities | Received quantities → 3-way matching.

## Standard checklist
- Create RFQ, confirm PO; amounts with Input VAT 7%
- Two-step approval: PO ≥ threshold goes To Approve; approver group can **Approve Order**; under threshold confirms directly
- Vendor pricelist (min qty, validity) auto price
- Receive partial → backorder created / no backorder
- Bill on received qty: bill qty = received; bill from PO vs manual bill matched to PO
- Over-receipt / receive more than ordered
- Cancel PO after receipt (blocked / warning)
- Replenishment (min/max) → auto RFQ [CONFIG]
- Purchase agreement: blanket order price used in RFQ
- Permission: purchase user can't approve above limit
- Integration: receipt stock in; Bill JE Dr Expense/Stock Interim / Dr Input VAT / Cr AP; landed cost [CONFIG]
- Report: print PO PDF Thai, vendor tax ID & branch
