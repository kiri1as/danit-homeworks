import sys
import unittest

from test_add_numbers import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add_numbers(2, 2), 4)

    def test_negative(self):
        self.assertEqual(add_numbers(-10, -5), -15)

    def test_negative_positive(self):
        self.assertEqual(add_numbers(-8, 5), -3)

    def test_zero_count(self):
        self.assertEqual(add_numbers(0, 999), 999)

    def test_max_int(self):
        self.assertEqual(add_numbers(sys.maxsize, -sys.maxsize), 0)

    def test_max_int_oversize(self):
            self.assertEqual(add_numbers(sys.maxsize, sys.maxsize), sys.maxsize*2)

    def test_max_float(self):
        self.assertEqual(add_numbers(sys.float_info.max, -sys.float_info.max), 0)

    def test_max_float_oversize(self):
        self.assertEqual(add_numbers(sys.float_info.max*3, sys.float_info.max*2), sys.float_info.max*5)

    def test_correct_type_provided(self):
        with self.assertRaises(TypeError):
            add_numbers('ABC', 105)


if __name__ == "__main__":
    unittest.main()
