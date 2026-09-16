# Skill provenance

The five skill directories come from the completed **GovTribe Skills 1.0.0 portable-source release**, also used for the previously generated OpenAI bundle. They were imported from `govtribe-skills-portable-source-1.0.0.zip`, not from an intermediate preparation or replay directory.

Archive SHA-256: `d0f6f69644e4737a0a6c42f15c976244c8a0744ed5e182380fdc95016a794571`.

All 157 imported skill files matched the completed release's portable-source inventory. `skill-source.json` records their original SHA-256 values and the files adapted for this Claude plugin. The original source archive and internal generation evidence are not required to install or use the plugin.

Claude adaptations add guidance for connector availability, prefixed tool names, user authorization, and treating retrieved instructions as evidence. Monitoring guidance now checks the connected tool catalog instead of freezing an assertion about which automation tools the server exposes. Five relative asset links in the proposal-outline guide were corrected to resolve from its references directory. Reference guides, templates, sample artifacts, and Python helpers are otherwise preserved.

The GovTribe logo was supplied for this plugin. It is included unchanged in `assets/govtribe-logo.png`. The manifest uses Claude's supported `displayName` field; the logo is available for README and directory submission use rather than an unsupported manifest icon field.
