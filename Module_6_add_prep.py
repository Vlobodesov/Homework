class Figure:
    # Базовый класс для всех фигур. Хранит общие свойства и методы.
    sides_count = 0  # Количество сторон фигуры, переопределяется в дочерних классах.

    def __init__(self, color, *sides):
        # Инициализация фигуры: установка цвета и сторон.
        # Если количество сторон не совпадает с sides_count, создаётся список сторон с единичными значениями.
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        # Установка цвета: проверка корректности цвета через метод __is_valid_color.
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False  # По умолчанию фигура не закрашена.

    def __is_valid_color(self, r, g, b):
        # Служебный метод для проверки корректности цвета.
        # Цвет корректен, если r, g, b - целые числа в диапазоне [0, 255].
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        # Устанавливает новый цвет фигуры, если он корректен.
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        # Возвращает текущий цвет фигуры в формате RGB.
        return self.__color

    def __is_valid_sides(self, *sides):
        # Служебный метод для проверки корректности списка сторон.
        # Количество сторон должно совпадать с sides_count, и все стороны должны быть положительными целыми числами.
        return (
            len(sides) == self.sides_count and
            all(isinstance(side, int) and side > 0 for side in sides)
        )

    def set_sides(self, *new_sides):
        # Устанавливает новые стороны фигуры, если они корректны.
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        # Возвращает текущий список сторон фигуры.
        return self.__sides

    def __len__(self):
        # Возвращает периметр фигуры (сумму всех сторон).
        return sum(self.__sides)


class Circle(Figure):
    # Класс круга. Унаследован от Figure.
    sides_count = 1  # У круга только одна "сторона" - длина окружности.

    def __init__(self, color, *sides):
        # Инициализация круга с передачей цвета и длины окружности.
        super().__init__(color, *sides)
        # Радиус рассчитывается из длины окружности (длина / 2π).
        self.__radius = self.get_sides()[0] / (2 * 3.14159)

    def get_square(self):
        # Возвращает площадь круга, используя формулу πr^2.
        return 3.14159 * self.__radius ** 2


class Triangle(Figure):
    # Класс треугольника. Унаследован от Figure.
    sides_count = 3  # У треугольника три стороны.

    def get_square(self):
        # Возвращает площадь треугольника, используя формулу Герона.
        a, b, c = self.get_sides()  # Получаем стороны треугольника.
        s = (a + b + c) / 2  # Полупериметр треугольника.
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Формула Герона.


class Cube(Figure):
    # Класс куба. Унаследован от Figure.
    sides_count = 12  # У куба 12 рёбер.

    def __init__(self, color, *sides):
        # Инициализация куба с передачей цвета и длины стороны.
        if len(sides) == 1:
            # Если передана только одна сторона, создаём список из 12 одинаковых сторон.
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        # Возвращает объём куба, используя формулу V = a^3 (где a - длина ребра).
        side = self.get_sides()[0]  # Все стороны равны, берём первую.
        return side ** 3


# Проверка кода
circle1 = Circle((200, 200, 100), 10)  # Создаём круг с заданным цветом и длиной окружности.
cube1 = Cube((222, 35, 130), 6)  # Создаём куб с заданным цветом и длиной стороны.

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменяем цвет круга на корректный.
print(circle1.get_color())  # Ожидается: [55, 66, 77]


cube1.set_color(300, 70, 15)  # Пытаемся задать некорректный цвет (r > 255), цвет не изменится.
print(cube1.get_color())  # Ожидается: [222, 35, 130]

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Пытаемся изменить стороны куба, количество сторон не совпадает с 12, изменение не произойдёт.
print(cube1.get_sides())  # Ожидается: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменяем длину окружности круга на 15.
print(circle1.get_sides())  # Ожидается: [15]

# Проверка периметра (длины окружности)
print(len(circle1))  # Ожидается: 15

# Проверка объёма куба
print(cube1.get_volume())  # Ожидается: 216 (6^3)

