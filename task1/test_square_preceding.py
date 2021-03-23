""" testing module square_preceding """
import unittest
from square_preceding import square_preceding


class TestSquare(unittest.TestCase):
    """ test for square_preceding function """
    def test_list_with_nums(self):
        """ test an list with random nums """
        expected = [0, 1, 4., 9]
        lst = [1, 2., -3, 6]
        square_preceding(lst)
        actual = lst
        self.assertEqual(expected, actual, "list with any nums")

    def test_empty_list(self):
        """ test an empty list """
        expected = []
        lst = []
        square_preceding(lst)
        actual = lst
        self.assertEqual(expected, actual, "empty list")

    def test_list_of_equal_vals(self):
        """ test an list of equal vals """
        expected = [0, 1, 1, 1, 1]
        lst = [1, 1, 1, 1, 1]
        square_preceding(lst)
        actual = lst
        self.assertEqual(expected, actual, "list of equal vals")


if __name__ == '__main__':
    unittest.main()
