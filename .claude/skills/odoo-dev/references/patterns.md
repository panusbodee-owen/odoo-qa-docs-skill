# Patterns (write for the target version; adjust per versions.md)

## Model
```python
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

class MyModel(models.Model):
    _name = "my.model"
    _description = "My Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]   # only if chatter needed
    _order = "date desc, id desc"
    _check_company_auto = True

    name = fields.Char(required=True, tracking=True)
    company_id = fields.Many2one("res.company", required=True, default=lambda s: s.env.company)
    partner_id = fields.Many2one("res.partner", check_company=True)
    line_ids = fields.One2many("my.model.line", "parent_id")
    amount_total = fields.Monetary(compute="_compute_amount_total", store=True)
    currency_id = fields.Many2one(related="company_id.currency_id")
    state = fields.Selection([("draft", "Draft"), ("done", "Done")], default="draft", tracking=True)

    @api.depends("line_ids.amount")
    def _compute_amount_total(self):
        for rec in self:
            rec.amount_total = sum(rec.line_ids.mapped("amount"))

    @api.constrains("amount_total")
    def _check_amount(self):
        for rec in self:
            if rec.amount_total < 0:
                raise ValidationError(_("Total cannot be negative."))

    def action_done(self):
        if self.filtered(lambda r: r.state != "draft"):
            raise UserError(_("Only draft records can be validated."))
        self.write({"state": "done"})
```
Extend existing: `_inherit = "sale.order"` (no `_name`), override with `super()`; keep signature, return super's result.

## Views (v18 syntax; v16/17 use `<tree>`, v16 uses `attrs`)
```xml
<record id="view_my_model_list" model="ir.ui.view">
  <field name="name">my.model.list</field><field name="model">my.model</field>
  <field name="arch" type="xml"><list><field name="name"/><field name="state" widget="badge"/></list></field>
</record>
<record id="view_sale_order_form_inherit_my" model="ir.ui.view">
  <field name="name">sale.order.form.inherit.my</field><field name="model">sale.order</field>
  <field name="inherit_id" ref="sale.view_order_form"/>
  <field name="arch" type="xml">
    <field name="partner_id" position="after"><field name="x_ref" invisible="state != 'draft'"/></field>
  </field>
</record>
```
Prefer `position` on named fields/`xpath` with `@name`, never on string labels or positional indexes.

## Security
`security/ir.model.access.csv`:
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model user,model_my_model,base.group_user,1,1,1,0
```
Multi-company record rule: domain `[('company_id', 'in', company_ids)]`. Load order in manifest: security groups XML → csv → rules → views → menus.

## Wizard (TransientModel)
Fields + `action_confirm`; open with `ir.actions.act_window` `target="new"`; pass records via `context={'active_ids': ...}` and read `self.env.context.get('active_ids')`.

## Cron
`data/ir_cron.xml` with `model_id`, `state="code"`, `code="model._cron_do()"`, `interval_number`, `interval_type`. Method must be idempotent and batch-limited (`limit=`), commit-free.

## QWeb PDF report
`ir.actions.report` (report_type `qweb-pdf`) + template calling `web.external_layout`; loop `docs`. Custom paper format via `report.paperformat`. Thai: see `l10n-th.md`.

## Controller / API
`@http.route('/api/x', type='json', auth='user')` (or `auth='api_key'`-style via custom check); `csrf=False` only for external `type='http'` POST with own auth. Use `request.env`, never sudo() without explicit access checks.

## Performance
Avoid N+1: `mapped`, `read_group`/`_read_group`, `search_read` with fields; `with_context(prefetch_fields=False)` for huge loops; index `index=True` for searched fields.
