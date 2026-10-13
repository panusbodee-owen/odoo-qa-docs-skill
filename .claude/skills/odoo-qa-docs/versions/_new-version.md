# Procedure: unknown or newer Odoo version (v19, v20, …)

Goal: keep working now, learn the deltas once, store them so later runs cost no extra tokens.

1. No `versions/vNN.md` → copy the table format of `v17.md` into a new `vNN.md`, Status: PARTIAL.
2. Write the deliverable with the v18 baseline; tag every menu path, button and field name `(verify)`. Never present unverified UI names as fact.
3. Verify (cheapest first, stop when enough):
   a. User-supplied screenshots / release notes / FSD.
   b. Live instance via an Odoo MCP/agent if available: read `ir.ui.menu` complete names and model fields for the modules in scope.
   c. Web search official release notes only if user allows.
4. Write ONLY confirmed differences into `vNN.md` (one row each: Area | Change | Confirmed? | Source). Do not copy unchanged baseline content.
5. Remove `(verify)` tags in the deliverable for confirmed items.
6. When a version becomes the main one for projects, the user may promote it to baseline: update `modules/*.md`, then turn the old baseline into a delta file.
