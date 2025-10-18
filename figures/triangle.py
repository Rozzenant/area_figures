import math
from area_figures.base.base import Shape
from typing import Tuple


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        sides: Tuple[float, float, float] = tuple(sorted([a, b, c]))
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть больше 0")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Неверные стороны треугольника")
        self._sides: Tuple[float, float, float] = sides
        self.a: float = a
        self.b: float = b
        self.c: float = c

    def area(self) -> float:
        """Формула Герона для вычисления площади любого треугольника"""
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self) -> bool:
        """Возвращает True, если треугольник прямоугольный"""
        a, b, c = self._sides
        return math.isclose(a**2 + b**2, c**2, rel_tol=1e-9)
