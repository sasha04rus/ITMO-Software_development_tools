import unittest

from geometric_lib import square

class SquareTestCase(unittest.TestCase):
    def test_area_zero_val(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_float_val(self):
        res = square.area(10.5)
        self.assertEqual(res, 10.5 ** 2)

    def test_area_big_val(self):
        res = square.area(123456789)
        self.assertEqual(res, 123456789 ** 2)

    def test_perimeter_big_val(self):
        res = square.perimeter(123456789)
        self.assertEqual(res, 123456789 * 4)

    def test_perimeter_zero_value(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)