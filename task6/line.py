""" module with Point and Line classes """
from typing import List


class Point:
    """ class Point """

    def __init__(self, x_coord: int or float, y_coord: int or float):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __str__(self):
        """ return str(self) """
        return f'({self.x_coord}, {self.y_coord})'

    def __eq__(self, other):
        """ return self == other """
        if isinstance(other, self.__class__):
            return (self.x_coord == other.x_coord) and\
                   (self.y_coord == other.y_coord)
        else:
            return False


class Line:
    """ class Line """
    def __init__(self, points: List[Point]):
        if points[0] == points[1]:
            raise ValueError('this line can\'t be built (point1 == point2)')
        self.point1 = points[0]
        self.point2 = points[1]
        # a*x + b*y = c
        self.a_coef = self.point2.y_coord - self.point1.y_coord
        self.b_coef = self.point1.x_coord - self.point2.x_coord
        self.c_coef = self.point1.x_coord * self.point2.y_coord -\
                      self.point2.x_coord * self.point1.y_coord

    def __eq__(self, other):
        """ return self == other """
        if isinstance(other, self.__class__):
            return (self.point1 == other.point1) and\
                   (self.point2 == other.point2)
        else:
            return False

    def __str__(self):
        """ return str(self) """
        sign = '-' if self.b_coef < 0 else '+'
        return f'{self.a_coef}*x {sign} {abs(self.b_coef)}*y = {self.c_coef}'

    def intersect(self, other):
        """ return point of intersection of two lines """
        if isinstance(other, self.__class__):
            try:
                x_cross = (
                                      other.b_coef * self.c_coef - other.c_coef * self.b_coef) /\
                          (
                                      other.b_coef * self.a_coef - other.a_coef * self.b_coef)
                y_cross = (
                                      other.c_coef * self.a_coef - other.a_coef * self.c_coef) /\
                          (
                                      other.b_coef * self.a_coef - other.a_coef * self.b_coef)
                x_cross = round(x_cross, 7)
                if x_cross == int(x_cross):
                    x_cross = int(x_cross)
                y_cross = round(y_cross, 7)
                if y_cross == int(y_cross):
                    y_cross = int(y_cross)

                res = Point(x_cross, y_cross)
            except ZeroDivisionError:
                if self.b_coef*other.c_coef == other.b_coef*self.c_coef and\
                        self.a_coef*other.c_coef == other.a_coef*self.c_coef:
                    res = self
                else:
                    res = None
        else:
            raise TypeError('not correct type of other object')
        return res
