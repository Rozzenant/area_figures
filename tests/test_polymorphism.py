import math
from area_figures.figures import Circle, Triangle
from area_figures.base.base import Shape


def test_polymorphic_area_calculation():
    shapes: list[Shape] = [
        Circle(1),
        Triangle(3, 4, 5),
    ]
    areas = [shape.area() for shape in shapes]
    assert math.isclose(areas[0], math.pi, rel_tol=1e-9)
    assert math.isclose(areas[1], 6.0, rel_tol=1e-9)