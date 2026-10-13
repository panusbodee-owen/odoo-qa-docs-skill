#!/usr/bin/env python3
"""Create a version-correct Odoo module skeleton.

Usage: scaffold.py MODULE --version 18 [--model x.model] [--depends base,mail] [--path .] [--author NAME]
Prints only the created file list.
"""
import argparse
import os
import sys


def main():
    p = argparse.ArgumentParser()
    p.add_argument("module")
    p.add_argument("--version", type=int, default=18)
    p.add_argument("--model", default=None, help="main model, e.g. x.request (default: <module>.record)")
    p.add_argument("--depends", default="base,mail")
    p.add_argument("--path", default=".")
    p.add_argument("--author", default="")
    a = p.parse_args()

    v = a.version
    mod = a.module
    model = a.model or f"{mod.replace('_', '.')}"
    if "." not in model:
        model += ".record"
    m_us = model.replace(".", "_")
    cls = "".join(w.capitalize() for w in model.replace(".", "_").split("_"))
    depends = [d.strip() for d in a.depends.split(",") if d.strip()]
    mail = "mail" in depends
    list_tag = "list" if v >= 18 else "tree"
    view_mode = "list,form" if v >= 18 else "tree,form"
    root = os.path.join(a.path, mod)
    if os.path.exists(root):
        sys.exit(f"{root} already exists")

    if v >= 18 and mail:
        chatter = "<chatter/>"
    elif mail:
        chatter = ('<div class="oe_chatter"><field name="message_follower_ids"/>'
                   '<field name="activity_ids"/><field name="message_ids"/></div>')
    else:
        chatter = ""
    if v >= 17:
        btn_vis = 'invisible="state != \'draft\'"'
    else:
        btn_vis = 'attrs="{\'invisible\': [(\'state\', \'!=\', \'draft\')]}"'
    if v >= 19:
        constraint = "    _name_company_uniq = models.Constraint(\n        \"UNIQUE(name, company_id)\", \"Name must be unique per company.\"\n    )  # (verify) v19 API\n"
    else:
        constraint = "    _sql_constraints = [\n        (\"name_company_uniq\", \"UNIQUE(name, company_id)\", \"Name must be unique per company.\"),\n    ]\n"
    inherit = '    _inherit = ["mail.thread", "mail.activity.mixin"]\n' if mail else ""
    tracking = ", tracking=True" if mail else ""

    files = {
        "__init__.py": "from . import models\n",
        "__manifest__.py": f'''{{
    "name": "{mod.replace('_', ' ').title()}",
    "version": "{v}.0.1.0.0",
    "summary": "",
    "author": "{a.author}",
    "license": "LGPL-3",
    "category": "Uncategorized",
    "depends": {depends!r},
    "data": [
        "security/ir.model.access.csv",
        "views/{m_us}_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": False,
}}
''',
        "models/__init__.py": f"from . import {m_us}\n",
        f"models/{m_us}.py": f'''from odoo import _, api, fields, models
from odoo.exceptions import UserError


class {cls}(models.Model):
    _name = "{model}"
    _description = "{cls}"
{inherit}    _order = "id desc"
    _check_company_auto = True

    name = fields.Char(required=True{tracking})
    company_id = fields.Many2one("res.company", required=True, default=lambda self: self.env.company)
    state = fields.Selection(
        [("draft", "Draft"), ("done", "Done")], default="draft", required=True{tracking}
    )
{constraint}
    def action_done(self):
        if self.filtered(lambda r: r.state != "draft"):
            raise UserError(_("Only draft records can be validated."))
        self.write({{"state": "done"}})
''',
        "security/ir.model.access.csv": (
            "id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n"
            f"access_{m_us}_user,{model} user,model_{m_us},base.group_user,1,1,1,0\n"
            f"access_{m_us}_manager,{model} manager,model_{m_us},base.group_system,1,1,1,1\n"),
        f"views/{m_us}_views.xml": f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_{m_us}_{list_tag}" model="ir.ui.view">
        <field name="name">{model}.{list_tag}</field>
        <field name="model">{model}</field>
        <field name="arch" type="xml">
            <{list_tag}>
                <field name="name"/>
                <field name="company_id" groups="base.group_multi_company"/>
                <field name="state" widget="badge"/>
            </{list_tag}>
        </field>
    </record>

    <record id="view_{m_us}_form" model="ir.ui.view">
        <field name="name">{model}.form</field>
        <field name="model">{model}</field>
        <field name="arch" type="xml">
            <form>
                <header>
                    <button name="action_done" type="object" string="Done" class="oe_highlight" {btn_vis}/>
                    <field name="state" widget="statusbar"/>
                </header>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="company_id" groups="base.group_multi_company"/>
                    </group>
                </sheet>
                {chatter}
            </form>
        </field>
    </record>

    <record id="action_{m_us}" model="ir.actions.act_window">
        <field name="name">{cls}</field>
        <field name="res_model">{model}</field>
        <field name="view_mode">{view_mode}</field>
    </record>
</odoo>
''',
        "views/menus.xml": f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <menuitem id="menu_{mod}_root" name="{mod.replace('_', ' ').title()}" sequence="90"/>
    <menuitem id="menu_{m_us}" name="{cls}" parent="menu_{mod}_root" action="action_{m_us}" sequence="10"/>
</odoo>
''',
        "tests/__init__.py": f"from . import test_{m_us}\n",
        f"tests/test_{m_us}.py": f'''from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class Test{cls}(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.rec = cls.env["{model}"].create({{"name": "R1"}})

    def test_action_done(self):
        self.rec.action_done()
        self.assertEqual(self.rec.state, "done")
        with self.assertRaises(UserError):
            self.rec.action_done()
''',
    }
    for rel, content in files.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(path)


if __name__ == "__main__":
    main()
