from src.square import Square
import pytest

from src.triangle import Triangle


@pytest.mark.parametrize(("side_a", "area", "perimeter"), [(3, 9, 12)])
def test_square(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == f"Square with side {side_a}"
    assert r.area == area
    assert r.perimeter == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"), [(0, 0, 0), (-3, 9, -12)])
def test_square_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        r = Square(side_a)
        assert r.name == f"Square {side_a}"
        assert r.area == area
        assert r.perimeter == perimeter


def test_add_area():
    s = Square(3)
    t = Triangle(3, 3, 3)
    assert s.add_area(t) == 12.897114317029974
