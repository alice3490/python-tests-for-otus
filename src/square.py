from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Cant create Square")
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = f"Square with side {side_a}"

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()

