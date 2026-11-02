import unittest
from scripts.validate_fixtures import validate, VALID_LOSS

class FixtureValidatorTests(unittest.TestCase):
    def test_current_fixtures_are_structurally_valid(self):
        files, errors = validate()
        self.assertGreaterEqual(len(files), 8)
        self.assertEqual(errors, [])

    def test_loss_taxonomy(self):
        self.assertEqual(VALID_LOSS, {"preserved", "transformed", "dropped", "unsupported", "ambiguous", "unsafe_widening"})

if __name__ == "__main__":
    unittest.main()
