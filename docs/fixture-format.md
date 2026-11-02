# Fixture Format

Fixtures are JSON test cases, not a universal memory schema.

Required fields: fixture_id, title, status, category, description, source_memory, migration, expected, loss_classification, notes.

Fixture status: draft, reviewed, observed, retired.

Fixtures express expected outcomes, not measured behavior. JSON shape equality alone does not prove semantic equivalence.
