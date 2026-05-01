import unittest
import finance


class TestCompoundInterest(unittest.TestCase):

    def test_compound_interest_valid(self):
        self.assertEqual(
            finance.compound_interest(1000, 0.1, 2),
            1210.0
        )

    def test_negative_rate_raises_error(self):
        with self.assertRaises(ValueError):
            finance.compound_interest(1000, -0.1, 2)

    def test_years_less_than_one_raises_error(self):
        with self.assertRaises(ValueError):
            finance.compound_interest(1000, 0.1, 0)


if __name__ == "__main__":
    unittest.main()
