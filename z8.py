from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name

    def draw(self):
        """Метод для отрисовки фигуры символами"""
        return f"[Фигура: {self.name}]"

    def __add__(self, other):
        """Перегрузка оператора сложения"""

        print("Результат сложения фигур:")
        '''print("Первая фигура:")
        print(self.draw())
        print("\nВторая фигура:")
        print(other.draw())
        print("\nСумма фигур:")'''

        # Создаем новую строку, которая объединяет отрисовки
        result_drawing = combine_drawings(self.draw(), other.draw())
        print(result_drawing)

        # Возвращаем новый объект с объединенным именем
        return Shape(f"Combined_{self.name}_{other.name}")


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
        self.versh = 0

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."

    def draw(self):
        """Отрисовка квадрата символами"""
        if self.length <= 0:
            return "[]"

        result = []
        size = min(self.length, 20)  # Ограничиваем размер для отображения

        # Верхняя граница
        result.append('┌' + '─' * size + '┐')

        # Стороны
        for _ in range(size):
            result.append('│' + ' ' * size + '│')

        # Нижняя граница
        result.append('└' + '─' * size + '┘')

        # Подпись
        result.append(f"Квадрат со стороной {self.length}")
        return '\n'.join(result)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        self.versh = 0

    def area(self):
        return pi * self.radius**2

    def draw(self):
        """Отрисовка круга символами"""
        if self.radius <= 0:
            return "○"

        result = []
        r = min(self.radius, 10)  # Ограничиваем радиус для отображения

        # Рисуем круг символами
        for y in range(-r, r + 1):
            line = []
            for x in range(-2 * r, 2 * r + 1):
                # Уравнение окружности (с учетом пропорций символов в терминале)
                if (x / 2) ** 2 + y ** 2 <= r ** 2:
                    line.append('●')
                else:
                    line.append(' ')
            result.append(''.join(line))

        # Подпись
        result.append(f"Круг с радиусом {self.radius}")
        return '\n'.join(result)


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
        self.versh = 3

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def fact(self):
        return "Длина любой стороны треугольника меньше суммы двух других"

    def draw(self):
        """Отрисовка треугольника символами"""
        result = []
        height = 6  # Фиксированная высота для отображения

        # Рисуем равнобедренный треугольник
        for i in range(height):
            spaces = height - i - 1
            stars = 2 * i + 1
            result.append(' ' * spaces + '/' + ' ' * (stars - 2) + '\\' if i < height - 1 else ' ' * spaces + '─' * stars)

        # Основание
        #result.append(' ' * (height - 1) + '| |')

        # Подпись
        result.append(f"Треугольник со сторонами {self.a}, {self.b}, {self.c}")
        return '\n'.join(result)


def combine_drawings(drawing1, drawing2):
    """Объединяет два рисунка в один"""
    lines1 = drawing1.split('\n')
    lines2 = drawing2.split('\n')

    max_len = max(len(lines1), len(lines2))

    # Дополняем списки строк до одинаковой длины
    while len(lines1) < max_len:
        lines1.append('')
    while len(lines2) < max_len:
        lines2.append('')

    # Находим максимальную ширину для первого рисунка
    max_width1 = max(len(line) for line in lines1) if lines1 else 0

    # Объединяем с разделителем
    combined = []
    for line1, line2 in zip(lines1, lines2):
        padding = ' ' * (max_width1 - len(line1))
        combined.append(line1 + padding + '   +   ' + line2)

    return '\n'.join(combined)


# Пример использования
if __name__ == "__main__":
    # Создаем фигуры
    square = Square(4)
    circle = Circle(3)
    triangle = Triangle(3, 4, 5)

    # Демонстрация сложения фигур
    print("Пример 1: Квадрат + Круг")
    result1 = square + circle

    print("\n" + "=" * 50 + "\n")

    print("Пример 2: Круг + Треугольник")
    result2 = circle + triangle

    print("\n" + "=" * 50 + "\n")

    print("Пример 3: Треугольник + Квадрат")
    result3 = triangle + square
