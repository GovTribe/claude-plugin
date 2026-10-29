# Proposal Compliance & Control

Use after selecting `proposal-control-workbook`.

1. **Read the workbook first.** Inspect Start Here, each working sheet's instructions, headers and dropdowns. The template explains its controls; the [sheet and field map](proposal-control-workbook-schema.md) locates them.
2. **Reuse the requirements.** Start with the current source inventory, requirement register and amendments. For missing or changed requirements, use **Solicitation Intelligence and Compliance Extraction** (`govtribe-proposal-workflows` → `references/solicitation-intelligence-and-compliance-extraction.md`, from that skill's installed root).
3. **Populate connected controls.** Fill Sources and Opportunity Setup, then the requirements, evaluation, submission, pricing/deliverables, questions and amendment tabs. Keep source and requirement IDs stable and propagate changes across linked controls. Record actual owners, evidence and response locations; distinguish compliance from drafting progress using the existing dropdowns.
4. **Check and deliver.** Recalculate and reconcile Dashboard counts with the working rows. Preserve formulas, validations and print panels. When extending print ranges, update their matching `PrintEnd*` defined names so Dashboard's print-coverage check stays accurate. Use [Template adaptation and revision checks](template-adaptation-and-revisions.md) for selected revisions, saved-sheet inspection and delivery.

For an optional structure check, run from the installed `govtribe-proposal-workflows` root (Python and `openpyxl` required):

```bash
python3 scripts/validate_proposal_workbook.py working.xlsx
```

This checks the eleven-sheet template's structure, selected formula bindings and print setup. Use native spreadsheet checks for custom layouts; source coverage, calculations and visual quality still need inspection.

For a selected workbook revision, grow changed wrapped rows inside its retained
print panels without replacing widths, print settings, formulas or embedded
objects. From the installed `govtribe-proposal-workflows` root:

```bash
python3 scripts/prepare_proposal_workbook_render.py revised.xlsx --previous-workbook selected-original.xlsx --output revised-readable.xlsx
```

Keep the selected original unchanged. This mode sizes only changed wrapped text
in visible working sheets' existing print areas; unchanged text, hidden content
and cells outside those panels are left alone. Its sizes are estimates: inspect
the saved output's affected normal-print panels at readable scale and confirm
the final lines fit. A separately prepared fit-to-width preview does not verify
the retained layout. For custom layouts or unsupported rotated/vertically merged
text, use native row sizing and inspect the result. Reconcile calculations after
content edits; row sizing itself preserves existing formula caches.
