# liskov_substitution


class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    def calcurate_area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, size) -> None:
        self._width = self._height = size

    @Rectangle.width.setter
    def width(self, size):
        self._width = self._height = size

    @Rectangle.height.setter
    def height(self, size):
        self._width = self._height = size


def print_area(obj):
    change_to_width = 10
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height

    print(f"予想面積 = {change_to_height* change_to_width},実際面積={obj.calcurate_area()}")


rc = Rectangle(2, 3)
print_area(rc)

# リスコフの置換原則に反する
sq = Square(5)
print_area(sq)
