from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(name='Triangle')
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or (side_a + side_b) <= side_c:
            raise ValueError("Cant create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle with sides {side_a}, {side_b} and {side_c}"
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def get_area(self):
        sp = self.get_perimeter() / 2
        return (sp * (sp - self.side_a) * (sp - self.side_b) * (sp - self.side_c)) ** 0.5

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()
