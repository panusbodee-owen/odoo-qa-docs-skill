# Version rules (cumulative: a rule applies to its version and every later one)

| Since | Rule | Old (do not use) | New |
|---|---|---|---|
| 15 | Assets declared in manifest | `<template inherit_id="web.assets_backend">` | `'assets': {'web.assets_backend': ['my_mod/static/src/**/*']}` |
| 16 | OWL components, JS as ES modules | legacy `odoo.define` widgets | `/** @odoo-module **/` + `import`, OWL `Component` |
| 17 | View modifiers are Python expressions | `attrs="{'invisible': [('state','!=','draft')]}"`, `states="draft"` | `invisible="state != 'draft'"`, `readonly="..."`, `required="..."` |
| 17 | Display name | `name_get()` override | `_compute_display_name()` with `@api.depends(...)` |
| 17 | Group check helper | `self.user_has_groups('base.group_user')` | `self.env.user.has_group('base.group_user')` |
| 17 | `create` decorator | `@api.model def create(self, vals)` | `@api.model_create_multi def create(self, vals_list)` |
| 18 | List view tag | `<tree>`, `view_mode="tree,form"` | `<list>`, `view_mode="list,form"` |
| 18 | Chatter | `<div class="oe_chatter"><field name="message_ids"/>…</div>` | `<chatter/>` |
| 18 | Field aggregation attr | `group_operator="sum"` | `aggregator="sum"` |
| 18 | Product type | `detailed_type`, `type == 'product'` | `type in ('consu','service','combo')` + `is_storable` |
| 19 | SQL constraints (verify) | `_sql_constraints = [(...)]` | `_name_uniq = models.Constraint('UNIQUE(name)', 'msg')` |
| 19 | Domains (verify) | `from odoo.osv import expression` | `from odoo.fields import Domain` |

Notes
- 16: `@api.model_create_multi` already preferred; `attrs` still valid.
- `check_compat.py` encodes this table; when adding a row, add the matching regex in `RULES` there.
- Unknown version (20+): apply all rows, mark unverified names `(verify)`, then add confirmed rows here with "Since = 20".
