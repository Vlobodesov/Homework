class Figure:
    sides_count = 0

    def __init__(self, filled):
        filled = True
        self.__sides = []
        self.__color = [0,0,0]

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if r in range(0, 255):
            if g in range(0, 255):
                if b in range(0, 255):
                    return True
        else:
            print('Такого цвета не существует')

    def set_color(self,r,g,b):
        self.__color = [r,g,b]

    def __is_valid_sides(self, *sides):
        for s in self.*sides:
            if isinstance(s, int) and s > 0 and len(self.*sides) = len(self.__sides):
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return

    def set_sides(self, *new_sides):
        # isinstance(*new_sides, list):
        if len(self.*new_sides) = self.sides_count:
            self.*new_sides = self.__sides


class Circle(Figure):
    sides_count = 1
    # self.__radius =  2 * 3.14 * ?
    #
    # def get_square(self):
    #     return 3.14 * ^2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
#

class Cube(Figure):
    sides_count = 12

    def get_sides(self):
        self.__sides = [0,0,0,0,0,0,0,0,0,0,0,0]
        return self.__sides

    def get_volume(self):
        return 

















