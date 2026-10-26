import unittest

import square


def get_area(side: int | float) -> int | float:
    return side * side


def get_perimeter(side: int | float) -> int | float:
    return 4 * side


class TestSquareArea(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(square.area(2), get_area(2))

    def test_normal_input2(self):
        self.assertEqual(square.area(5.5), get_area(5.5))

    def test_normal_input3(self):
        self.assertEqual(square.area(10.333), get_area(10.333))

    def test_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_string(self):
        with self.assertRaises(TypeError):
            square.area("1")

    def test_none(self):
        with self.assertRaises(TypeError):
            square.area(None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            square.area(False)

        with self.assertRaises(TypeError):
            square.area(True)


class TestSquarePerimeter(unittest.TestCase):
    def test_normal_input1(self):
        self.assertEqual(square.perimeter(2), get_perimeter(2))

    def test_normal_input2(self):
        self.assertEqual(square.perimeter(5.5), get_perimeter(5.5))

    def test_normal_input3(self):
        self.assertEqual(square.perimeter(10.333), get_perimeter(10.333))

    def test_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1)

    def test_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("1")

    def test_none(self):
        with self.assertRaises(TypeError):
            square.perimeter(None)

    def test_bool(self):
        with self.assertRaises(TypeError):
            square.perimeter(False)

        with self.assertRaises(TypeError):
            square.perimeter(True)
