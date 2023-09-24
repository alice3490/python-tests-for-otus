from src.rectangle import Rectangle
import pytest

from src.square import Square


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"), [(3, 5, 15, 16)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle with sides {side_a} and {side_b}"
    assert r.area == area
    assert r.perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"), [(-3, -5, 15, 16), (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle with sides {side_a} and {side_b}"
        assert r.area == area
        assert r.perimeter == perimeter


def test_add_area():
    r = Rectangle(3, 5)
    s = Square(3)
    assert r.add_area(s) == 24

