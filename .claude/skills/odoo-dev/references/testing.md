# Testing & debugging

## Unit test (`tests/__init__.py` imports each `test_*.py`)
```python
from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged

@tagged("post_install", "-at_install")
class TestMyModel(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "C001"})
        cls.rec = cls.env["my.model"].create({"name": "R1", "partner_id": cls.partner.id})

    def test_done_only_from_draft(self):
        self.rec.action_done()
        self.assertEqual(self.rec.state, "done")
        with self.assertRaises(UserError):
            self.rec.action_done()
```
- Access rights: `self.rec.with_user(user).read()` inside `assertRaises(AccessError)`; create users with `new_test_user(self.env, login='u', groups='base.group_user')` from `odoo.tests.common`.
- Forms like the UI: `from odoo.tests import Form` → `with Form(self.env['sale.order']) as f: ...` (triggers onchange).
- UI tours: `HttpCase` + `self.start_tour("/odoo", "tour_name", login="admin")` (v16/17 url `/web`).
- Map each QA test case (TC-xx from odoo-qa-docs) to one `test_` method when automating.

## Commands
```bash
odoo-bin -c odoo.conf -d test_db -i my_module --test-enable --stop-after-init            # install + tests
odoo-bin -c odoo.conf -d test_db -u my_module --test-tags /my_module --stop-after-init     # only this module
odoo-bin -c odoo.conf -d test_db --test-tags /my_module:TestMyModel.test_done_only_from_draft
odoo-bin shell -c odoo.conf -d db        # interactive env
odoo-bin -c odoo.conf --dev=all          # reload XML/py, show qweb errors
```
Use a disposable DB for tests (never production). Log level: `--log-level=debug_sql` for SQL issues.

## Debugging checklist
1. Reproduce with a test or `odoo-bin shell` snippet.
2. Read the full traceback bottom-up; locate the custom module frame.
3. View errors: `--dev=xml` and check the inherited view's xpath target still exists in this version.
4. Access errors: check `ir.model.access.csv`, record rules, `check_company`.
5. After fix: add a regression test.
