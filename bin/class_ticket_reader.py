from collections import defaultdict


class TicketReader:
    """
    This class which manages tickets
    """
    __tickets = []
    __tickets_count = 0
    __remaining_tickets = 0
    __slot_by_color = defaultdict(set)
    __number_by_color = defaultdict(set)
    __slot_by_number = {}
    __ticket_by_slot = {}

    def __init__(self, ticket):
        self.__tickets = ticket
        self.__tickets_count = len(ticket)
        self.__remaining_tickets = len(ticket)
        self.__slot_by_color = defaultdict(set)
        self.__number_by_color = defaultdict(set)
        self.__car_by_number = {}
        self.__ticket_by_slot = {}

    def get_ticket_count(self):
        return self.__tickets_count

    def get_tickets(self):
        return self.__tickets

    def get_remaining_tickets(self):
        return self.__remaining_tickets

    def issue_ticket(self):
        self.__remaining_tickets -= 1
        return self.__tickets.pop(0)

    def return_ticket(self, ticket):
        self.__remaining_tickets += 1
        self.__tickets.insert(ticket.get_ticket_id() - 1, ticket)

    def save_car_location(self, car_number, car_color, slot_id, ticket):
        self.__slot_by_color[car_color].add(slot_id)
        self.__number_by_color[car_color].add(car_number)
        self.__slot_by_number.setdefault(car_number, slot_id)
        self.__ticket_by_slot.setdefault(slot_id, ticket)

    def remove_car_location(self, allotted_slot):
        car_details = allotted_slot.get_car_details()
        slot_id = allotted_slot.get_slot_id()
        car_color = car_details.get_car_color()
        car_number = car_details.get_car_number()
        self.__slot_by_color[car_color].remove(slot_id)
        self.__number_by_color[car_color].remove(car_number)
        self.__slot_by_number.pop(car_number)
        self.__ticket_by_slot.pop(slot_id)
        if len(self.__slot_by_color[car_color]) == 0:
            self.__slot_by_color.pop(car_color)
        if len(self.__number_by_color[car_color]) == 0:
            self.__number_by_color.pop(car_color)

    def get_slots_by_color(self, car_color):
        return_value = self.__slot_by_color.get(car_color, False)
        if return_value:
            print("\n", *return_value)
        else:
            print("\n", "Not Found!!")

    def get_car_number_by_color(self, car_color):
        return_value = self.__number_by_color.get(car_color, False)
        if return_value:
            print("\n", *return_value)
        else:
            print("\n", "Not Found!!")

    def get_slot_by_car_number(self, car_number):
        print("\n", self.__slot_by_number.get(car_number, "Not Found!!"))

    def get_ticket_by_slot(self, slot_id):
        return self.__ticket_by_slot[slot_id]

    def get_allotted_tickets(self):
        return self.__ticket_by_slot.items()
