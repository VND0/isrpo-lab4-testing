import unittest

import triangle


def get_area(a, h):
    return a * h / 2


def get_perimeter(a, b, c):
    return a + b + c


class TestTriangleArea(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(triangle.area(2, 3), get_area(2, 3))

    def test_normal_input2(self):
        self.assertEqual(triangle.area(5.5, 2.5), get_area(5.5, 2.5))

    def test_normal_input3(self):
        self.assertEqual(triangle.area(10.333, 4.2), get_area(10.333, 4.2))

    def test_zero_side_a(self):
        self.assertEqual(triangle.area(0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(triangle.area(5, 0), 0)

    def test_negative_side_a(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            triangle.area(5, -1)

    def test_string(self):
        with self.assertRaises(TypeError):
            triangle.area("1", 5)

        with self.assertRaises(TypeError):
            triangle.area(5, "1")

    def test_none(self):
        with self.assertRaises(TypeError):
            triangle.area(None, 5)

        with self.assertRaises(TypeError):
            triangle.area(5, None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            triangle.area(False, 5)

        with self.assertRaises(TypeError):
            triangle.area(True, 5)

        with self.assertRaises(TypeError):
            triangle.area(5, False)

        with self.assertRaises(TypeError):
            triangle.area(5, True)


class TestTrianglePerimeter(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(triangle.perimeter(2, 3, 4), get_perimeter(2, 3, 4))

    def test_normal_input2(self):
        self.assertEqual(
            triangle.perimeter(5.5, 2.5, 3.5), get_perimeter(5.5, 2.5, 3.5)
        )

    def test_normal_input3(self):
        self.assertEqual(
            triangle.perimeter(10.333, 4.2, 7.1), get_perimeter(10.333, 4.2, 7.1)
        )

    def test_zero_side_a(self):
        self.assertEqual(triangle.perimeter(0, 5, 4), get_perimeter(0, 5, 4))

    def test_zero_side_b(self):
        self.assertEqual(triangle.perimeter(5, 0, 4), get_perimeter(5, 0, 4))

    def test_zero_side_c(self):
        self.assertEqual(triangle.perimeter(5, 4, 0), get_perimeter(5, 4, 0))

    def test_zero_all_sides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_negative_side_a(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, 5, 4)

    def test_negative_side_b(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(5, -1, 4)

    def test_negative_side_c(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(5, 4, -1)

    def test_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("1", 5, 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, "1", 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, 4, "1")

    def test_none(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(None, 5, 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, None, 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, 4, None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(False, 5, 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(True, 5, 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, False, 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, True, 4)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, 4, False)

        with self.assertRaises(TypeError):
            triangle.perimeter(5, 4, True)
