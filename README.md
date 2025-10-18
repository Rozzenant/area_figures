# area_figures

Библиотека на Python для вычисления площади геометрических фигур:
- Круг (`Circle`)
- Треугольник (`Triangle`) с определением прямоугольности
- Единый интерфейс (`Shape`) с полиморфным `.area()`

## Клонирование

```bash
git clone -b main https://github.com/Rozzenant/area_figures.git
cd area_figures
```

# 1. Создание и активация виртуального окружения
```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac
```

# 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

# 3. Запуск тестов с покрытием
```bash
pytest tests/ --cov=area_figures --cov-report=term-missing
```

# 4. Проверка форматирования
```bash
black --check .
flake8
```
