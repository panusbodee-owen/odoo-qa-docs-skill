# Accounting / Invoicing — Thailand (baseline: Odoo 18 — apply `versions/vNN.md` deltas for other versions)

Menus: `Accounting > Customers > Invoices | Credit Notes | Payments` · `Accounting > Vendors > Bills | Refunds | Payments` · `Accounting > Accounting > Journal Entries | Journal Items` · Bank reconcile from `Accounting > Dashboard` (bank journal) · `Accounting > Reporting > Balance Sheet | Profit and Loss | General Ledger | Aged Receivable | Aged Payable | Tax Return` (EE reports) · `Accounting > Configuration > Settings | Taxes | Journals | Chart of Accounts`
Flow: Draft → **Confirm** (Posted) → **Register Payment** → Paid / In Payment → reconcile with bank statement. Reverse: **Credit Note** / **Reverse Entry**. **Reset to Draft** if allowed.

Thai localization `l10n_th` [CONFIG]: Thai CoA, VAT 7% sales/purchase taxes, tax report. Items often from OCA/custom — confirm with user before writing TC:
- Withholding tax (WHT 1/2/3/5%), WHT certificate (50 Tawi), WHT returns PND 3 / PND 53
- Tax invoice / receipt / billing note layouts, branch number (Head Office / Branch 00001)
- Undue output/input VAT (VAT on services, recognized on payment) → Odoo **Cash Basis** taxes (Settings > Taxes > Cash Basis)
- Input/output VAT reports and VAT return (PP 30)

## Standard checklist
- Invoice post: JE Dr AR / Cr Revenue / Cr Output VAT; sequence numbering per journal/year
- Bill post: Dr Expense / Dr Input VAT / Cr AP; duplicate vendor reference warning
- Payment full / partial / overpayment; payment difference write-off; batch payment [CONFIG]
- Cash-basis VAT: undue VAT account moves to VAT account on payment
- WHT on payment: net paid = gross − WHT, WHT payable account, certificate print [CONFIG]
- Credit note full/partial reverses VAT
- Foreign currency invoice; exchange gain/loss on payment
- Bank statement import & reconcile; reconciliation models [CONFIG]
- Lock dates: posting into locked period blocked
- Fiscal positions (exempt / 0% export)
- Permission: Billing vs Accountant vs Adviser rights
- Reports tie-out: GL, AR/AP aging, tax report totals = sum of posted taxes
