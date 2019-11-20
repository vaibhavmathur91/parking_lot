class Car:
    """
    The class is for the cars
    """
    __color = None
    __number = None

    def __init__(self, color, number):
        self.__color = color
        self.__number = number

    def get_car_color(self):
        return self.__color

    def get_car_number(self):
        return self.__number
