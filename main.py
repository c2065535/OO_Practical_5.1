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
        return (self.w > (p.x)) & (self.l > (p.y))




if __name__ == "__main__":
    p = Point(10, 10) #FIX CONTAINS ERROR
    r = Rectangle(p, 4, 5)

    print(r.__contains__(p))
