# Claude-only template exclusion experiment

This is an alternative 1.2.0 candidate for directory validation only. It is not
submitted, published, or a replacement for the original held candidate.

Parent Claude commit: `b1611719f0d69c7a899b5ba5c85dd7c5b929cc2a`.
The permanent metadata PR retains all 158 imported files and all 15 masters.
This child removes only Annotated Proposal Outline's master, example, preview
and completion guide; six catalog/router/reference files are adapted so nothing
requests the omitted template. It retains seven skills, 154 skill files and
14 byte-identical template masters. Outline work can use the existing requirement
map and the host's native document capabilities.

`skill-source.json` records the exact candidate inventory, original omitted and
adapted hashes, upstream source digests and experimental status. Upstream archive
hashes identify the original input, not this candidate or a new approval.
The original held commit and the master remain preserved in Git history and the
shared authoring source. ChatGPT, GTAI and all shared sources are unchanged.

Local structural checks do not prove that Anthropic will clear its binary-file
hold. This experiment tests only whether omitting the named template changes the
directory finding. No new model tests, source rewrites, deployment or publication
are part of it.
