import math
import pytest
from area_figures.figures import Circle


def test_circle_area():
    circle = Circle(2)
    assert math.isclose(circle.area(), math.pi * 4, rel_tol=1e-9)

def test_circle_zero():
    with pytest.raises(ValueError):
        Circle(0)

def test_circle_negative():
    with pytest.raises(ValueError):
        Circle(-3)