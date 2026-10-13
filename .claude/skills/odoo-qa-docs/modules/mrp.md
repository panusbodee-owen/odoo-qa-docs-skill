# Manufacturing (baseline: Odoo 18 — apply `versions/vNN.md` deltas for other versions)

Menus: `Manufacturing > Operations > Manufacturing Orders | Unbuild Orders | Scrap` · `Manufacturing > Products > Bills of Materials` · `Manufacturing > Configuration > Settings | Work Centers | Operations`
Flow: BoM → MO **Confirm** → **Check Availability** → (Work Orders start/finish) → **Produce All** → Done. Components consumed, finished goods in stock.
States: Draft → Confirmed → In Progress → To Close → Done / Cancelled

Settings [CONFIG]: Work Orders, Subcontracting, By-Products, Lots & Serials, Quality (EE), MPS (EE), Lock quantities.
BoM type: Manufacture this product | Kit | Subcontracting. BoM **Flexible Consumption**: Allowed | Allowed with warning | Blocked.

## Standard checklist
- MO from BoM: component qty × MO qty; multi-level BoM creates child MOs [CONFIG]
- Component shortage: availability Waiting; partial production → backorder MO
- Consumption differs from BoM → follows Flexible Consumption rule
- Lot/serial on finished good and components; traceability report
- Work orders: time tracking, work center capacity/cost
- By-products produced; scrap during MO
- Kit BoM: delivery explodes components
- Unbuild order reverses production
- Replenishment Manufacture route → MO auto created
- Cost: finished good cost = components + operation cost (AVCO/FIFO); JE WIP/Stock [CONFIG]
