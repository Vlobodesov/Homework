class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)


    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        return f'Модель: {self.__model}'
        return f'Мощность двигателя: {self.__engine_power}'
        return f'Цвет: {self.__color}'
        return f'Владелец: {self.owner}'

    def set_color(self, new_color):
        color_v = [i.upper() for i in self.__COLOR_VARIANTS]
        new_color = str(new_color)
        if new_color.upper() in color_v:
            new_color = self.__color
        else:
            return f'Нельзя сменить цвет на {new_color}'



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'

vehicle1.print_info()