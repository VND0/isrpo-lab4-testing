# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Описание функций
Каждый из файлов `.py` содержит две функции, вычисляющие площадь или периметр некоторой геометрической фигуры.

## circle.py

### area(r: float) -> float
*Вычисляет площадь круга.*

Параметры:
- r (`float`): радиус круга

Выходные данные:

`float` - площадь круга с радиусом r.

Примеры использования:

```python
>>> area(2)
12.566370614359172

>>>area(0)
0.0
```

### perimeter(r: float) -> float
*Вычисляет длину окружности.*

Параметры:
- r (`float`): радиус окружности

Выходные данные:

`float` - длина окружности с радиусом r

Примеры использования:

```python
>>> perimeter(2)
12.566370614359172

>>> perimeter(0)
0.0
```

## rectangle.py

### area(a: float, b: float) -> float
*Вычисляет площадь прямоугольника.*

Параметры:
- a (`float`): длина одной стороны
- b (`float`): длина стороны, смежной a

Выходные данные:

`float` - площадь прямоугольника

Примеры использования:

```python
>>> area(1, 2)
2

>>> area(10.5, 31.1)
326.55
```

### perimeter(a: float, b: float) -> float
*Вычисляет периметр прямоугольника.*

Параметры:
- a (`float`): длина одной стороны
- b (`float`): длина стороны, смежной a

Выходные данные:

`float` - периметр прямоугольника

Примеры использования:

```python
>>> perimeter(2, 4)
12

>>> perimeter(21, 36)
114
```

## square.py

### area(a: float) -> float
*Вычисляет площадь квадрата.*

Параметры:
- a (`float`): длина стороны

Возвращаемое значение:

`float` - площадь квадрата

Примеры использования:

```python
>>> area(2)
4

>>> area(25)
625
```

### perimeter(a: float) -> float
*Вычисляет периметр квадрата.*

Параметры:
- a (`float`): длина стороны

Возвращаемое значение:

`float` - периметр квадрата

Примеры использования:

```python
>>> perimeter(2)
8

>>> perimeter(100.5)
402.0
```

## triangle.py

### area(a: float, h: float) -> float
*Вычисляет площадь треугольника.*

Параметры:
- a (`float`): сторона треугольника
- h (`float`): высота, проведенная к стороне a

Возвращаемое значение:

`float` - площадь треугольника

Примеры использования:

```python
>>> area(3, 4)
6.0

>>> area(10.1, 14.9)
75.245
```

### perimeter(a: float, b: float, c: float) -> float
*Вычисляет периметр треугольника.*

Параметры:
- a (`float`): сторона треугольника
- b (`float`): другая сторона треугольника
- c (`float`): третья сторона треугольника

Возвращаемое значение:

`float` - периметр треугольника

Примеры использования:

```python
>>> perimeter(3, 4, 5)
12

>>> perimeter(432789, 21389, 1290)
455468
```

# История изменений в репозитории
```
* 1234fe3 (HEAD -> new_features_558498) Added usage examples
* 2bd260f Added docs for functions
* 1a9d8ad Added docstrings for all functions
* dcb83ee Fixed perimeter formula
* b89e2db Added triangle.py
* 318ea78 Added rectangle.py
| * 86edb1c (origin/release) L-05: Update Docs. Add user agreement info
| * 438b89a L-05: Add user agreement
| * 6adb962 L-03: Docs added
| | * 3049431 (origin/feature) L-04: Add rectangle.py
| |/  
|/|   
| | * b5b0fae (origin/develop) L-04: Update docs for calculate.py
| | * d76db2a L-04: Add calculate.py
| | * 51c40eb L-04: Doc updated for triangle
| | * d080c78 L-04: Triangle added
| |/  
|/|   
* | d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
|/  
* 8ba9aeb L-03: Circle and square added
```
