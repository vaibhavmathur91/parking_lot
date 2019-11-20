class Level:
    """
    The class is the levels of the parking lot
    """
    __level_id = 0
    __slots = {}
    __slots_count = 0

    def __init__(self, slots_of_each_level, level_id):
        self.__level_id = level_id
        self.__slots = slots_of_each_level
        self.__slots_count = len(slots_of_each_level)

    def get_level_id(self):
        return self.__level_id

    def get_slots(self):
        """
        The method to get the spacesOfEachLevel in the level
        """
        return self.__slots

    def get_slots_count(self):
        """
        The method to get the space count of the level
        """
        return self.__slots_count
