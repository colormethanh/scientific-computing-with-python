class Retangle():

    """
    A simple class that makes a retangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return (f"Retangle(width={self.width}, height={self.height})")

    def set_width(self, n_width):
        self.width = n_width

    def set_height(self, n_height):
        self.height = n_height

    def get_area(self):
        return(self.width * self.height)

    def get_perimeter(self):
        return((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        return(((self.width ** 2) + (self.height ** 2)) ** .5)

    def get_picture(self):
        rows = []
        if self.width > 50 or self.height > 50:
            return("Too big for picture.")
        else:
            for r in range(self.height):
                row = []

                for c in range(self.width):
                    row.append("*")
                row.append("\n")
                rows.append("".join(row))
        return("".join(rows))

    def get_amount_inside(self, n_rect):
        (w, h) = (
            (self.width // n_rect.width),
            (self.height // n_rect.height)
        )
        amount_inside = w * h

        return(amount_inside)


class Square(Retangle):
    """
    Class that makes a Square
    """

    def __init__(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def __str__(self):
        return(f"Square(side={self.side})")

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height


rect = Retangle(16, 8)
print(rect)
print(rect.get_picture())


n_rect = Retangle(4, 4)
print(n_rect)
print(n_rect.get_picture())

print(rect.get_amount_inside(n_rect))

sqr = Square(4)
print(sqr)

sqr.set_width(5)
print(sqr.height)
print(sqr)
