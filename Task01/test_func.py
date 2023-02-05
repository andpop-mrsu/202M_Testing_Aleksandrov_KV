import unittest
from triangle_func import IncorrectTriangleSides, get_triangle_type


class TestTriangleFunction(unittest.TestCase):

    def test_type_error(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", "b", "c")

    def test_incorrect_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(10, 10, 10), 'equilateral')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(10, 12, 14), 'nonequilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(10, 10, 19), 'isosceles')


if __name__ == '__main__':
    unittest.main()
