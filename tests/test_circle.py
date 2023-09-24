from src.circle import Circle
import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize(("radius", "area", "length"), [(3, 28.26, 18.84)])
def test_circle(radius, area, length):
    c = Circle(radius)
    assert c.name == f"Circle with radius {radius}"
    assert c.area == area
    assert c.length == length


@pytest.mark.parametrize(("radius", "area", "length"), [(0, 0, 0), (-1, 1, 1)])
def test_circle_negative(radius, area, length):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert c.name == f"Circle with radius {radius}"
        assert c.area == area
        assert c.length == length


def test_add_area():
    c = Circle(3)
    r = Rectangle(3, 5)
    assert c.add_area(r) == 43.260000000000005

