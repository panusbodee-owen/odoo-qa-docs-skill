#!/usr/bin/env python3
"""Scan an Odoo module for patterns that are deprecated/removed in the target version.

Usage: check_compat.py MODULE_PATH --version 18
Output: one line per hit `file:line  RULE  hint`, then a count. Exit 1 if hits.
Keep RULES in sync with references/versions.md.
"""
import argparse
import ast
import os
import re
import sys

# (since_version, rule, file_ext, regex, hint)
RULES = [
    (15, "assets-xml", ".xml", r'inherit_id="web\.assets_(backend|frontend|common)"', "declare assets in __manifest__ 'assets'"),
    (16, "legacy-js", ".js", r"\bodoo\.define\(", "use ES module + /** @odoo-module **/"),
    (17, "attrs", ".xml", r"\battrs\s*=", "use invisible/readonly/required python expressions"),
    (17, "states-attr", ".xml", r"<(field|button)\b[^>]*\bstates\s*=", "use invisible=\"state not in (...)\""),
    (17, "name_get", ".py", r"def\s+name_get\s*\(", "override _compute_display_name"),
    (17, "user_has_groups", ".py", r"\.user_has_groups\(", "self.env.user.has_group(...)"),
    (17, "create-single", ".py", r"@api\.model\s*\n\s*def\s+create\s*\(", "@api.model_create_multi def create(self, vals_list)"),
    (18, "tree-tag", ".xml", r"<tree\b|</tree>", "use <list>"),
    (18, "view_mode-tree", ".xml", r'name="view_mode"[^<]*>[^<]*\btree\b', "use list in view_mode"),
    (18, "view_mode-tree", ".py", r"""['"]view_mode['"]\s*:\s*['"][^'"]*\btree\b""", "use 'list' in view_mode"),
    (18, "oe_chatter", ".xml", r'class="oe_chatter"', "use <chatter/>"),
    (18, "group_operator", ".py", r"\bgroup_operator\s*=", "use aggregator="),
    (18, "detailed_type", ".py", r"\bdetailed_type\b", "product: type + is_storable"),
    (18, "detailed_type", ".xml", r"\bdetailed_type\b", "product: type + is_storable"),
    (18, "type-product", ".py", r"""type\s*==\s*['"]product['"]""", "use is_storable"),
    (19, "sql_constraints", ".py", r"\b_sql_constraints\s*=", "models.Constraint (verify)"),
    (19, "osv-expression", ".py", r"from\s+odoo\.osv\s+import\s+expression|odoo\.osv\.expression", "odoo.fields.Domain (verify)"),
]


def manifest_version(path):
    mf = os.path.join(path, "__manifest__.py")
    try:
        with open(mf, encoding="utf-8") as f:
            v = ast.literal_eval(f.read()).get("version", "")
        return int(v.split(".")[0]) if v.count(".") >= 4 else None
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("path")
    p.add_argument("--version", type=int, default=None)
    a = p.parse_args()
    target = a.version or manifest_version(a.path) or 18
    rules = [(r, ext, re.compile(rx), h) for s, r, ext, rx, h in RULES if s <= target]
    hits = 0
    for dirpath, dirs, files in os.walk(a.path):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__", "migrations")]
        for fn in files:
            ext = os.path.splitext(fn)[1]
            fp = os.path.join(dirpath, fn)
            active = [r for r in rules if r[1] == ext]
            if not active:
                continue
            with open(fp, encoding="utf-8", errors="ignore") as f:
                text = f.read()
            for rule, _, rx, hint in active:
                for m in rx.finditer(text):
                    line = text.count("\n", 0, m.start()) + 1
                    print(f"{fp}:{line}  {rule}  {hint}")
                    hits += 1
    mv = manifest_version(a.path)
    if mv and mv != target:
        print(f"{a.path}/__manifest__.py  manifest-version  version starts with {mv}, target {target}")
        hits += 1
    print(f"target v{target}: {hits} issue(s)")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
