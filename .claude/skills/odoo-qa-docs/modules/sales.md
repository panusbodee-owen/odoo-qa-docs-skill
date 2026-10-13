# Sales (baseline: Odoo 18 — apply `versions/vNN.md` deltas for other versions)

Menus: `Sales > Orders > Quotations | Orders` · `Sales > To Invoice > Orders to Invoice` · `Sales > Products > Products | Pricelists` · `Sales > Configuration > Settings`
Flow: Quotation → **Send by Email** → **Confirm** (Sales Order) → Delivery (Inventory) → **Create Invoice** → Invoice **Confirm** → **Register Payment**
States: Quotation → Quotation Sent → Sales Order → (Locked) / Cancelled

Settings that change behavior [CONFIG]: Discounts, Pricelists, Quotation Templates, Online Signature/Payment, Lock Confirmed Sales, Pro-Forma Invoice, Margins, Customer credit limit (Accounting settings), Variants, UoM.
Product: Invoicing Policy = Ordered quantities | Delivered quantities (drives what can be invoiced).
Create Invoice wizard: Regular invoice | Down payment (percentage) | Down payment (fixed amount).

## Standard checklist
- Create/confirm SO; amounts Untaxed / VAT 7% / Total; rounding per line vs global [CONFIG]
- Pricelist & discount applied; quotation template + optional products; validity date expiry
- Delivered-qty policy: invoice blocked until delivery validated; partial delivery → partial invoice
- Down payment then final invoice deducts down payment
- Cancel SO with delivery done (expect warning/blocked); Lock / Unlock
- Credit limit warning on customer over limit [CONFIG]
- Multi-UoM, product variants, archived product not selectable
- Permission: `User: Own Documents Only` cannot see others' SO; `Administrator` sees settings
- Negative: no customer → required error; qty 0 / negative; price below cost (margin)
- Integration: SO → DO created (storable goods), Invoice JE: Dr AR / Cr Revenue / Cr Output VAT
- Report: print Quotation/SO PDF, Thai text & company/branch info [CONFIG]
