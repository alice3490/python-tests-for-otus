from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
import pytest

from src.triangle import Triangle


@pytest.mark.parametrize(("side_a", "area", "perimeter"), [(0, 0, 0), (-3, 9, -12)],
                         ids=["The length of side is equal to zero",
                              "The length of side is less than zero"
                              ]
                         )
def test_square_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        r = Square(side_a)
        assert r.name == f"Square {side_a}"
        assert r.area == area
        assert r.perimeter == perimeter


@pytest.mark.parametrize(("figure", "result"), [
    (Circle(3), 43.260000000000005),
    (Rectangle(3, 5), 24),
    (Triangle(3, 3, 3), 18.897114317029974)],
                         ids=["square area + circle area",
                              "square area + rectangle area",
                              "square area + triangle area"])
def test_add_area(figure, result):
    s = Square(3)
    t = Triangle(3, 3, 3)
    assert s.add_area(t) == 12.897114317029974
