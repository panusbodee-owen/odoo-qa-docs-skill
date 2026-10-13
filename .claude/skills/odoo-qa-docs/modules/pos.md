# Point of Sale (baseline: Odoo 18 — apply `versions/vNN.md` deltas for other versions)

Menus: `Point of Sale > Dashboard` (Open Register / Continue Selling) · `Point of Sale > Orders > Orders | Sessions | Payments` · `Point of Sale > Products > Products` · `Point of Sale > Configuration > Settings | Point of Sales | Payment Methods`
Flow: Open session (opening cash) → add products → **Payment** → choose method → **Validate** → receipt → **Close Register** (cash count) → session posted JE.

Settings [CONFIG]: Payment Methods (Cash, Bank/Card, QR PromptPay via bank), Pricelists, Discounts, Loyalty/Promotions/Gift cards, Invoicing from POS, Restaurant (floors/tables, kitchen printer), Fiscal position, Stock: real-time vs at closing.

## Standard checklist
- Sale cash with change; split payment cash + card
- Customer requests tax invoice → Invoice option, customer with Tax ID/branch
- Refund/return order; refund to original method
- Discount line/global, pricelist per customer, promotion/loyalty points
- Offline mode then sync (verify)
- Cash in/out; closing cash difference posted to difference account
- Close session: JE summarized per payment method; stock moves created
- Permissions: cashier vs manager (price change, discount, refund) [CONFIG]
- Receipt print layout Thai, VAT included price display
