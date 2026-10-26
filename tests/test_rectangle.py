import unittest

import rectangle


def get_area(a, b):
    return a * b


def get_perimeter(a, b):
    return (a + b) * 2


class TestRectangleArea(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(rectangle.area(2, 3), get_area(2, 3))

    def test_normal_input2(self):
        self.assertEqual(rectangle.area(5.5, 2.5), get_area(5.5, 2.5))

    def test_normal_input3(self):
        self.assertEqual(rectangle.area(10.333, 4.2), get_area(10.333, 4.2))

    def test_zero_side_a(self):
        self.assertEqual(rectangle.area(0, 5), 0)

    def test_zero_side_b(self):
        self.assertEqual(rectangle.area(5, 0), 0)

    def test_negative_side_a(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)

    def test_negative_side_b(self):
        with self.assertRaises(ValueError):
            rectangle.area(5, -1)

    def test_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("1", 5)

        with self.assertRaises(TypeError):
            rectangle.area(5, "1")

    def test_none(self):
        with self.assertRaises(TypeError):
            rectangle.area(None, 5)

        with self.assertRaises(TypeError):
            rectangle.area(5, None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            rectangle.area(False, 5)

        with self.assertRaises(TypeError):
            rectangle.area(True, 5)

        with self.assertRaises(TypeError):
            rectangle.area(5, False)

        with self.assertRaises(TypeError):
            rectangle.area(5, True)


class TestRectanglePerimeter(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(rectangle.perimeter(2, 3), get_perimeter(2, 3))

    def test_normal_input2(self):
        self.assertEqual(rectangle.perimeter(5.5, 2.5), get_perimeter(5.5, 2.5))

    def test_normal_input3(self):
        self.assertEqual(rectangle.perimeter(10.333, 4.2), get_perimeter(10.333, 4.2))

    def test_zero_side_a(self):
        self.assertEqual(rectangle.perimeter(0, 5), get_perimeter(0, 5))

    def test_zero_side_b(self):
        self.assertEqual(rectangle.perimeter(5, 0), get_perimeter(5, 0))

    def test_zero_both_sides(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_negative_side_a(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, 5)

    def test_negative_side_b(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(5, -1)

    def test_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("1", 5)

        with self.assertRaises(TypeError):
            rectangle.perimeter(5, "1")

    def test_none(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(None, 5)

        with self.assertRaises(TypeError):
            rectangle.perimeter(5, None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(False, 5)

        with self.assertRaises(TypeError):
            rectangle.perimeter(True, 5)

        with self.assertRaises(TypeError):
            rectangle.perimeter(5, False)

        with self.assertRaises(TypeError):
            rectangle.perimeter(5, True)