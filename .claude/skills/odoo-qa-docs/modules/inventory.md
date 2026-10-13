# Inventory (baseline: Odoo 18 — apply `versions/vNN.md` deltas for other versions)

Menus: `Inventory > Operations > Transfers > Receipts | Deliveries` (Internal when multi-location) · `Inventory > Operations > Physical Inventory | Replenishment | Scrap` (verify for your edition) · `Inventory > Products > Products | Lots/Serial Numbers` · `Inventory > Reporting > Stock | Moves History | Moves Analysis | Valuation` · `Inventory > Configuration > Settings | Warehouses | Locations | Routes`
v18 product: Product Type = Goods | Service | Combo; **Track Inventory** checkbox; tracking By Quantity | By Lots | By Unique Serial Number.
Transfer states: Draft → Waiting → Ready → Done / Cancelled. Buttons: **Check Availability**, **Validate**, **Return**, backorder wizard (Create Backorder / No Backorder).

Settings [CONFIG]: Storage Locations, Multi-Step Routes (1/2/3 step receipt & delivery), Lots & Serial Numbers, Expiration Dates, Packages, UoM, Landed Costs, Reservation method on operation type.
Valuation (Product Category): Costing Method Standard | FIFO | AVCO; Inventory Valuation Manual | Automated.

## Standard checklist
- Receipt validate → On Hand increases; Delivery validate → decreases; reserved qty
- Partial with backorder / no backorder; return of receipt and delivery
- Lot/Serial: required on validate; duplicate serial blocked; expiry date FEFO [CONFIG]
- Multi-step routes: Input→Stock, Pick→Pack→Out documents chained
- Internal transfer between locations/warehouses
- Physical inventory: count → Apply → adjustment move + JE (Automated)
- Scrap → qty decreases, scrap location
- Negative stock: deliver more than on hand (allowed? per setting / location)
- Replenishment min/max rule triggers RFQ or MO
- UoM conversion purchase UoM ≠ stock UoM
- Valuation: AVCO/FIFO cost after receipts at different prices; automated JE Stock Valuation / Interim
- Reports: Stock, Moves History, Valuation match expected numbers
