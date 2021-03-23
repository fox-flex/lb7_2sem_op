""" module which test line module """
from unittest import TestCase
from unittest import main as unittest_run
from line import Point
from line import Line


class TestPoint(TestCase):
    def setUp(self) -> None:
        """ create values for testing """
        self.point1 = Point(1, 2)
        self.point2 = Point(1, 3)
        self.point0 = 'asjkjkndajkads'

    def test_init_str_eq(self):
        """ test methods init, str and eq """
        self.assertEqual(self.point1.x_coord, 1)
        self.assertEqual(self.point1.y_coord, 2)

        self.assertEqual(str(self.point1), '(1, 2)')

        self.assertTrue(self.point1 == self.point1)
        self.assertFalse(self.point1 == self.point2)
        self.assertFalse(self.point1 == self.point0)



class TestLine(TestCase):
    """ class TestLine """
    def setUp(self) -> None:
        """ create values for testing """
        # create values for testing Point
        self.point1 = Point(1, 2)
        self.point2 = Point(1, 3)
        self.point0 = 'asjkjkndajkad'
        # create values for testing Line
        self.line1 = Line([Point(0, 0), Point(1, 1)])  # 1*x - 1*y = 0
        self.line2 = Line([Point(1, 1), Point(3, 3)])  # 2*x - 2*y = 0
        self.line3 = Line([Point(0, 1), Point(1, 2)])  # 1*x - 1*y = -1
        self.line4 = Line([Point(2, 0), Point(0, 2)])  # 2*x + 2*y = 4
        self.line5 = Line([Point(1, 0), Point(0, 1)])  # 1*x + 1*y = 1
        self.line6 = Line([Point(0, 1), Point(1, 1)])  # 0*x - 1*y = -1
        self.line6_0 = Line([Point(0, 2), Point(1, 2)])  # 0*x - 1*y = -2
        self.line6_1 = Line([Point(0, 1), Point(2, 1)])  # 0*x - 2*y = -2
        self.line0 = 'ahahahhahahahahhawfhjasfhjgasdfhjgdsgfhjkdsgfhjkllk'

    # testing Point
    def test_init_str_eq(self):
        """ test methods init, str and eq """
        self.assertEqual(self.point1.x_coord, 1)
        self.assertEqual(self.point1.y_coord, 2)

        self.assertEqual(str(self.point1), '(1, 2)')

        self.assertTrue(self.point1 == self.point1)
        self.assertFalse(self.point1 == self.point2)
        self.assertFalse(self.point1 == self.point0)

    # testing Line
    def test_init(self):
        """ test method init """
        with self.assertRaises(ValueError):
            _ = Line([Point(1, 1), Point(1, 1)])
        self.assertEqual(self.line1.point1, Point(0, 0))
        self.assertEqual(self.line1.point2, Point(1, 1))
        self.assertEqual(self.line1.a_coef, 1)
        self.assertEqual(self.line1.b_coef, -1)
        self.assertEqual(self.line1.c_coef, 0)

    def test_str(self):
        """ test method str """
        self.assertEqual(str(self.line1), '1*x - 1*y = 0')
        line = Line([Point(2, 0), Point(0, 2)])
        self.assertEqual(str(line), '2*x + 2*y = 4')

    def test_eq(self):
        """ test method eq """
        self.assertTrue(self.line1 == self.line1)
        self.assertFalse(self.line1 == self.line2)
        self.assertFalse(self.line1 == self.line0)

    def test_intersect(self):
        """ test method intersect """
        with self.assertRaises(TypeError):
            _ = self.line1.intersect(self.line0)
        self.assertEqual(self.line6.intersect(self.line6_0), None)
        self.assertEqual(self.line6.intersect(self.line6_1), self.line6)
        self.assertEqual(self.line1.intersect(self.line2), self.line1)
        self.assertEqual(self.line1.intersect(self.line3), None)
        self.assertEqual(self.line1.intersect(self.line4), Point(1, 1))
        self.assertEqual(self.line1.intersect(self.line5), Point(0.5, 0.5))


if __name__ == '__main__':
    unittest_run()
