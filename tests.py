import unittest
from format_price import format_price


class TestPriceFormatter(unittest.TestCase):

    def test_space_separator(self):
        self.assertEqual(format_price('123456789.01'), '123 456 789.01')

    def test_zeros_after_decimal_point(self):
        self.assertEqual(format_price('1.000'), '1')

    def test_integer_input(self):
    	self.assertEqual(format_price(123456), '123 456')

    def test_float_input(self):
    	self.assertEqual(format_price(1234.123), '1 234.12')

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            format_price('ewr23')

    def test_invalid_type(self):
    	with self.assertRaises(ValueError):
    		format_price([1, 2])

if __name__ == '__main__':
    unittest.main()