import unittest
import dollarstonairaconversionfunction

class TestCurrencyCinversionFunction(unittest.TestCase):

    def test_whole_number_conversions(self):
        self.assertEqual(dollarstonairaconversionfunction.dollars_to_naira(20),17500.0)



