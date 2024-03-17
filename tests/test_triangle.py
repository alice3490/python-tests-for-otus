from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"), [(2, 1, 4, 1, 5), (0, 0, 0, 0, 0),
                                                                               (-1, -2, -1, 1, -4)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        r = Triangle(side_a, side_b, side_c)
        assert r.name == f"Triangle with sides {side_a}, {side_b} and {side_c}"
        assert r.area == area
        assert r.perimeter == perimeter


@pytest.mark.parametrize(("figure", "result"), [
    (Circle(3), 43.260000000000005),
    (Rectangle(3, 5), 24),
    (Square(3), 18.897114317029974)],
                         ids=["triangle area + circle area",
                              "triangle area + rectangle area",
                              "triangle area + square area"])
def test_add_area(figure, result):
    t = Triangle(3, 4, 5)
    c = Circle(3)
    assert t.add_area(c) == 34.260000000000005
