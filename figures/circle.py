import math
from area_figures.base.base import Shape


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self.radius: float = radius

    def area(self) -> float:
        """Вычисляет площадь круга"""
        return math.pi * self.radius**2
