import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'

    def __repr__(self):
        return self.x, self.y


class Rectangle:
    def __init__(self, o, w, l):
        self.o = o  # Origin: Point
        self.w = w      # Width
        self.l = l      # Length

    def __str__(self):
        return f'Origin = ({self.o.x}, {self.o.y}), W = {self.w}, L = {self.l}'

    def __repr__(self):
        return self.o.x, self.o.y, self.w, self.l

    def area(self):
        return self.w * self.l

    def perimeter(self):
        return (self.w * 2) + (self.l * 2)

    def __contains__(self, p):
        return (self.w > p.x) & (self.l > p.y)


class Circle:
    def __init__(self, o, r):
        self.o = o  # Origin : Point
        self.r = r  # Radius

    def __str__(self):
        return f'Origin: ({self.o.x}, {self.o.y}), Radius: {self.r}'

    def __repr__(self):
        return self.o.x, self.o.y, self.r

    def area(self):
        return self.r * math.pi

    def perimeter(self):
        return 2 * math.pi * self.r

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        # Adapted from
        # https://www.geeksforgeeks.org/find-if-a-point-lies-inside-or-on-circle/
        return ((p.x - self.o.x) ** 2 + (p.y - self.o.y) ** 2) <= (self.r ** 2)


class Curve():
    """Class to represent a list of points on a graph"""

    def __init__(self, *inputs):
        """constructor for a curve"""
        self.items = []
        for i in inputs:
            self.append_if_valid(i)

    def append_if_valid(self, item):
        """add a new point object to the curve"""
        if not isinstance(item, Point):
            raise TypeError("Curves only take point objects")
        self.items.append(item)

    def __str__(self):
        """string representation of a curve"""
        return "Curve:{}".format(self.items)

    def __repr__(self):
        """formal string representation of a curve"""
        s = ", "
        s = s.join([repr(x) for x in self.items])
        return "Curve({})".format(s)

    def __getitem__(self, index):
        """get point(s) in curve"""
        if isinstance(index, int):
            return self.items[index]
        else:
            return Curve(*self.items[index])

    def __setitem__(self, index, item):
        """update curve with given point value"""
        if not isinstance(item, Point):
            raise TypeError("Curves only take point objects")
        self.items[index] = item


if __name__ == "__main__":
    p = Point(10, 10)
    r = Rectangle(p, 4, 5)
    c = Circle(p, 4)

    print(c.perimeter())
