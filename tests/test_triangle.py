import math
import pytest
from area_figures.figures import Triangle


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-9)


def test_triangle_is_right():
    assert Triangle(3, 4, 5).is_right()


def test_triangle_not_right():
    assert not Triangle(3, 4, 6).is_right()


def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)


def test_triangle_negative_side():
    with pytest.raises(ValueError):
        Triangle(-1, 2, 2)


def test_triangle_zero_side():
    with pytest.raises(ValueError):
        Triangle(0, 2, 2)
