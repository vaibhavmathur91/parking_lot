class Ticket:
    """
    This class is the parking ticket
    """
    __ticket_id = 0
    __level_id = 0
    __slot_id = 0

    def __init__(self, ticket_id, level_id, slot_id):
        self.__ticket_id = ticket_id
        self.__level_id = level_id
        self.__slot_id = slot_id

    def get_ticket_id(self):
        return self.__ticket_id

    def get_level_id(self):
        return self.__level_id

    def get_slot_id(self):
        return self.__slot_id
