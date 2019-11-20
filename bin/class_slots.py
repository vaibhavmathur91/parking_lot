class Slots:
    """
    The class is the slot to park the cars in each level of the parking lot
    """
    __is_car_parked = False
    __slot_id = 0
    __parked_car = None

    def __init__(self, slot_id):
        self.__is_car_parked = False
        self.__slot_id = slot_id
        self.__parked_car = None

    def get_slot_id(self):
        return self.__slot_id

    def park_car(self, parked_car):
        """
        :details The method is to set the park-car-flag to true to execute the action of parking
        :param parked_car (object from Class CAR)
        """
        self.__is_car_parked = True
        self.__parked_car = parked_car

    def leave_car(self):
        """
        The method for cars leaving
        """
        self.__is_car_parked = False
        self.__parked_car = None

    def get_car_details(self):
        return self.__parked_car

    def is_car_parked(self):
        return self.__is_car_parked
