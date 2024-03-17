from src.circle import Circle
import pytest
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(("radius", "area", "length"), [(0, 0, 0), (-1, 1, 1)])
def test_circle_negative(radius, area, length):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert c.name == f"Circle with radius {radius}"
        assert c.area == area
        assert c.length == length


@pytest.mark.parametrize(("figure", "result"), [
    (Rectangle(3, 5), 43.260000000000005),
    (Square(3), 37.260000000000005),
    (Triangle(3, 3, 3), 32.15711431702998)],
                         ids=["circle area + rectangle area",
                              "circle area + square area",
                              "circle area + triangle area"])
def test_add_area(figure, result):
    c = Circle(3)
    assert c.add_area(figure) == result
