from src.circle import Circle
from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"), [(3, 4, 5, 6, 12),
                                                                               (2, 2, 1, 0.9682458365518543, 5),
                                                                               (3, 3, 3, 3.897114317029974, 9)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle with sides {side_a}, {side_b} and {side_c}"
    assert r.area == area
    assert r.perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"), [(2, 1, 4, 1, 5), (0, 0, 0, 0, 0),
                                                                               (-1, -2, -1, 1, -4)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        r = Triangle(side_a, side_b, side_c)
        assert r.name == f"Triangle with sides {side_a}, {side_b} and {side_c}"
        assert r.area == area
        assert r.perimeter == perimeter


def test_add_area():
    t = Triangle(3, 4, 5)
    c = Circle(3)
    assert t.add_area(c) == 34.260000000000005
