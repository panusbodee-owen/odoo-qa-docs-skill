# Thailand specifics

- **Baht text (amount in Thai words):** `self.currency_id.with_context(lang='th_TH').amount_to_text(amount)` uses num2words `th` when the language is installed (verify output format; customers often expect "…บาทถ้วน" / "…สตางค์"). If format differs, write a small helper and unit-test 0, 1, 11, 21, 101, 1,000,000.25.
- **Buddhist year:** in QWeb `<t t-esc="doc.date.year + 543"/>` or format day/month/(year+543) in a helper; keep DB dates Gregorian.
- **Thai font in PDF (wkhtmltopdf):** ship font in `static/src/fonts/` (e.g. Sarabun, OFL licence), declare `@font-face` in a SCSS added to `web.report_assets_common`, set `font-family` on report root. Test with long Thai text + line wrapping.
- **Tax ID:** 13 digits; checksum: sum(d[i]*(13-i) for i in 0..11) → (11 - sum % 11) % 10 == d[12]. Branch: `00000` = Head Office, else 5-digit branch code — usually a custom field on `res.partner` if the installed localization lacks it.
- **Address on tax invoice:** company & customer name, address, Tax ID, branch, "ต้นฉบับ/สำเนา" copies — typically a custom QWeb report.
- **WHT / PND3 / PND53 / 50 Tawi:** check whether the project uses OCA `l10n_thailand` modules or custom before writing new code; extend rather than duplicate.
- **Undue VAT on services:** standard Cash Basis taxes; do not build custom VAT reversal logic.
