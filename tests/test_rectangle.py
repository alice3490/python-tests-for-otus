from src.circle import Circle
from src.rectangle import Rectangle
import pytest

from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"), [(-3, -5, 15, 16), (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle with sides {side_a} and {side_b}"
        assert r.area == area
        assert r.perimeter == perimeter


@pytest.mark.parametrize(("figure", "result"), [
    (Circle(3), 43.260000000000005),
    (Square(3), 24),
    (Triangle(3, 3, 3), 18.897114317029974)],
                         ids=["rectangle area + circle area",
                              "rectangle area + square area",
                              "rectangle area + triangle area"])
def test_add_area(figure, result):
    r = Rectangle(3, 5)
    assert r.add_area(figure) == result
