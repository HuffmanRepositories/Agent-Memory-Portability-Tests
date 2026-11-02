# Migration Loss Taxonomy

- **preserved** — semantics and relevant metadata survive.
- **transformed** — explicit, documented representation change.
- **dropped** — information omitted.
- **unsupported** — target cannot represent data.
- **ambiguous** — evidence insufficient.
- **unsafe_widening** — scope, trust, or permissions expand harmfully.

Record the affected field, source/target behavior, and whether loss was expected. Multiple labels may apply. Do not mark migration as preserved solely because output is syntactically valid.
