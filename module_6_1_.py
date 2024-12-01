from idlelib.colorizer import color_config


class Vehicle():
    def __init__(self, owner: str, __model: str , __engine_power: int , __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return (f'Цвет: {self.__color}')

    def print_info(self):
        return print(self.get_model() + '\n' + self.get_horsepower() + '\n' + self.get_color()
              + '\n' + f'Владелец: {self.owner}')


    def set_color(self,new_color: str ):
        if new_color.upper() in [color_list.upper()
                                 for color_list in vehicle1.__COLOR_VARIANTS]:
                self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()