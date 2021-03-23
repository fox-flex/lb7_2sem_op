import unittest

from point_1 import Point
from unittest import TestCase
from unittest import main as unittest_run


class TestPoint(TestCase):
    def setUp(self):

        self.A = Point(5, 6)
        self.B = Point(6, 10)
        self.C = Point(5.0, 6.0)
        self.D = Point(-5, -6)

    def test_init(self):

        self.assertEqual((self.A.x, self.A.y), (float(5), float(6)), "Значення не дійсні числа!")
        self.assertEqual((self.B.x, self.B.y), (float(6), float(10)), "Значення не дійсні числа!")
        self.assertEqual((self.C.x, self.C.y), (float(5), float(6)), "Значення не дійсні числа!")
        self.assertEqual((self.D.x, self.D.y), (float(-5), float(-6)), "Значення не дійсні числа!")

    def test_str(self):

        self.assertTrue(str(self.A) == "(5.0, 6.0)",  "Неправильний вивід на екран!")
        self.assertTrue(str(self.B) == "(6.0, 10.0)", "Неправильний вивід на екран!")
        self.assertTrue(str(self.C) == "(5.0, 6.0)", "Неправильний вивід на екран!")
        self.assertTrue(str(self.D) == "(-5.0, -6.0)", "Неправильний вивід на екран!")

    def test_eq(self):

        self.assertTrue(self.A == self.C, "Дві однакові точки при тестуванні виявились не однаковими!")
        self.assertFalse(self.A == self.B,  "Дві різні точки при тестуванні виявилися однаковими!")
        self.assertFalse(self.A == self.D,   "Дві різні точки при тестуванні виявилися однаковими!!")

    def test_ne(self):

        self.assertFalse(self.A != self.C, "Дві однакові точки при тестуванні виявились не однаковими!")
        self.assertTrue(self.A != self.B, "Дві різні точки при тестуванні виявилися однаковими!")
        self.assertTrue(self.A != self.D, "Дві різні точки при тестуванні виявилися однаковими!")

    def test_move(self):

        self.assertEqual((self.A.x, self.A.y), (float(5), float(6)), "Значення не дійсні числа!")
        self.assertEqual((self.B.x, self.B.y), (float(6), float(10)), "Значення не дійсні числа!")
        self.assertEqual((self.C.x, self.C.y), (float(5), float(6)), "Значення не дійсні числа!")
        self.assertEqual((self.D.x, self.D.y), (float(-5), float(-6)), "Значення не дійсні числа!")

    def test_rotate(self):

        self.assertEqual(self.A.rotate(180, self.B), self.A.move(7, 14), "Неправильний результат обчислення повороту точки!")
        self.assertEqual(self.A.rotate(360, self.D), self.A.move(5, 6), "Неправильний результат обчислення повороту точки!")

    def test_get_xposition(self):

        self.assertEqual(self.A.x, float(5), "Значения x не дійсне число!")
        self.assertEqual(self.B.x, float(6), "Значения x не дійсне число!")
        self.assertEqual(self.C.x, float(5), "Значения x не дійсне число!")
        self.assertEqual(self.D.x, float(-5), "Значения x не дійсне число!")

    def test_get_yposition(self):

        self.assertEqual(self.A.y, float(6), "Значения y не дійсне число!")
        self.assertEqual(self.B.y, float(10), "Значения y не дійсне число!")
        self.assertEqual(self.C.y, float(6), "Значения y не дійсне число!")
        self.assertEqual(self.D.y, float(-6), "Значения y не дійсне число!")


if __name__ == '__main__':
    unittest_run()
