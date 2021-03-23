from math import pi, sin, cos, radians


class Point:
    'Represents a point in two-dimensional geometric coordinates'

    def __init__(self, x=0, y=0):

        '''Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin.'''
        self.move(x, y)

    def __str__(self):

        return '({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):

        if isinstance(other, self.__class__):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return NotImplemented  # False

    def __ne__(self, other):

        if isinstance(other, self.__class__):
            return (self.x != other.x) or (self.y != other.y)
        else:
            return NotImplemented  # False

    def move(self, x, y):

        "Move the point to a new location in 2D space."
        self.x = float(x)
        self.y = float(y)

    def rotate(self, beta, other_point):

        'Rotate point around other point'
        dx = self.x - other_point.get_xposition()
        dy = self.y - other_point.get_yposition()
        xpoint3 = dx * cos(beta) - dx * sin(beta)
        ypoint3 = dy * cos(beta) + dy * sin(beta)
        xpoint3 = xpoint3 + other_point.get_xposition()
        ypoint3 = ypoint3 + other_point.get_yposition()
        return self.move(xpoint3, ypoint3)

    def get_xposition(self):

        return self.x

    def get_yposition(self):

        return self.y
