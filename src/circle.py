class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Cant create circle')
        self.radius = radius
        self.pi = 3.14
        self.name = f"Circle with radius {radius}"
        self.area = self.get_area()
        self.length = self.get_length()

    def get_area(self):
        return self.pi * self.radius ** 2

    def get_length(self):
        return 2 * self.pi * self.radius

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()
