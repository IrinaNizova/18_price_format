from format_price import format_price
import unittest


class TestCasePrice(unittest.TestCase):
    def test_extra_zeros_case(self):
        self.assertEqual(format_price(1120.00), '1 120')

    def test_fraction_part_case(self):
        self.assertEqual(format_price(0.0140), '0.01')

    def test_big_price_case(self):
        self.assertEqual(format_price(1120000.10), '1 120 000.10')

    def test_string_case(self):
        self.assertEqual(format_price('120300'), '120 300')

    def test_letter_case(self):
        self.assertIsNone(format_price('120t00'))

    def test_list_case(self):
        self.assertIsNone(format_price([12000]))


if __name__ == '__main__':
    unittest.main()
