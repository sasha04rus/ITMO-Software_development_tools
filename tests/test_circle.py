import unittest
import math

from geometric_lib import circle

class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_float_val(self):
        res = circle.area(1.0)
        self.assertEqual(res, math.pi)

    def test_area_big_radius(self):
        res = circle.area(123456789)
        self.assertEqual(res, (123456789**2 * math.pi))

    def test_perimeter_zero_radius(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_big_value(self):
        res = circle.perimeter(123456789)
        self.assertEqual(res, (123456789 * 2 * math.pi))