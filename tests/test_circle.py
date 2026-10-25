import unittest
import math

import circle


def get_area(r: int | float) -> float:
    return math.pi * r * r


def get_circumference(r: int | float) -> float:
    return 2 * math.pi * r


class TestCircleArea(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(circle.area(10), get_area(10))

    def test_normal_input2(self):
        self.assertEqual(circle.area(25), get_area(25))

    def test_normal_input3(self):
        self.assertEqual(circle.area(0.0001), get_area(0.0001))

    def test_zero_radius(self):
        self.assertEqual(circle.area(0), get_area(0))

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_string(self):
        with self.assertRaises(TypeError):
            circle.area("hello world")

    def test_none(self):
        with self.assertRaises(TypeError):
            circle.area(None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            circle.area(True)

        with self.assertRaises(TypeError):
            circle.area(False)


class TestCirclePerimeter(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(circle.perimeter(10), get_circumference(10))

    def test_normal_input2(self):
        self.assertEqual(circle.perimeter(25), get_circumference(25))

    def test_normal_input3(self):
        self.assertEqual(circle.perimeter(0.001), get_circumference(0.001))

    def test_zero_radius(self):
        self.assertEqual(circle.perimeter(0), get_circumference(0))

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)

    def test_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("hello world")

    def test_none(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            circle.perimeter(True)

        with self.assertRaises(TypeError):
            circle.perimeter(False)
