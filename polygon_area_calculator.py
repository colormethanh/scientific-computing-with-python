class Retangle():

    """
    A simple class that makes a retangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return (f"Retangle(Width = {self.width}, Height = {self.height})")

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


rct = Retangle(10, 5)
print(rct.get_picture())

rct.set_height(50)
print("=" * 20)
print(rct.get_picture())
