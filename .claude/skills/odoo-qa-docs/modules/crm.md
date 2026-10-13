# CRM (baseline: Odoo 18 — apply `versions/vNN.md` deltas for other versions)

Menus: `CRM > Sales > My Pipeline | My Activities | My Quotations` · `CRM > Leads > Leads` (when Leads enabled) · `CRM > Reporting > Pipeline | Activities` · `CRM > Configuration > Settings | Sales Teams | Stages | Lost Reasons`
Flow: Lead → **Convert to Opportunity** → stages (drag in kanban) → **New Quotation** → **Won** / **Lost** (reason).

Settings [CONFIG]: Leads, Recurring Revenues, Multi Teams, Lead Enrichment/Generation, Predictive Lead Scoring, Assignment rules.

## Standard checklist
- Create lead manually / from email alias; duplicate detection & merge
- Convert to opportunity: link existing customer vs create new
- Stage change, expected revenue, probability
- Schedule activity, overdue activity shown
- New Quotation from opportunity → SO linked, quotation count
- Mark Won (probability 100%) / Lost with reason; restore
- Team assignment, salesperson sees own pipeline only [CONFIG]
- Pipeline report filters & group by
