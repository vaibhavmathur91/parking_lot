import sys, os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from bin.class_slots import Slots
from bin.class_level import Level
from bin.class_ticket_reader import TicketReader
from bin.class_tickets import Ticket
from bin.class_car import Car


class ParkingLot:
    """
    The class is the whole parking lot
    """

    __levels = []
    __ticket_reader = None
    __levelCount = 0
    __total_space_count = 0
    __slots_count_each_level = 0

    def __init__(self, total_spaces):
        self.__levelCount = 1
        new_tickets = []
        for i in range(self.__levelCount):
            level_id = i + 1
            self.__slots_count_each_level = total_spaces
            slots_of_each_level = {}
            for j in range(self.__slots_count_each_level):
                slot_id = i * self.__slots_count_each_level + j + 1
                slots_of_each_level.update({slot_id: Slots(slot_id)})
                new_tickets.append(Ticket(slot_id, level_id, slot_id))
            self.__levels.append(Level(slots_of_each_level, level_id))
            self.__total_space_count += self.__slots_count_each_level

        self.__ticket_reader = TicketReader(new_tickets)
        print("\nCreated a parking lot with " + str(total_spaces) + " slots")

    def allowed_to_park(self):
        """
        The method to check if the parking lot allow to park
        """
        return self.__ticket_reader.get_remaining_tickets() > 0

    def park(self, car_details):
        """
        :details To park the car in the position as the card says
        :param car_details (color, number)
        :return issued_ticket (object from Class Ticket)
        """
        if self.allowed_to_park():
            car_number = car_details[0]
            car_color = car_details[1]
            parked_car = Car(car_color, car_number)
            ticket = self.__ticket_reader.issue_ticket()
            level_id = ticket.get_level_id()
            slot_id = ticket.get_slot_id()
            print(" \nAllocated slot number: ", slot_id)
            self.__levels[level_id - 1].get_slots()[slot_id].park_car(parked_car)
            self.__ticket_reader.save_car_location(car_number, car_color, slot_id, ticket)
            return slot_id
        else:
            print("\nParking Full !!")


    def leave(self, slot_id):
        """
        :details The car leaves off the space
        :param slot_id
        """
        ticket = self.__ticket_reader.get_ticket_by_slot(int(slot_id))
        level_id = ticket.get_level_id()
        slot_id = ticket.get_slot_id()
        allotted_slot = self.__levels[level_id - 1].get_slots()[slot_id]
        self.__ticket_reader.remove_car_location(allotted_slot)
        self.__ticket_reader.return_ticket(ticket)
        allotted_slot.leave_car()
        print(" \nSlot number " + str(slot_id) + " is free")
        return slot_id

    def registration_numbers_for_cars_with_colour(self, car_color):
        self.__ticket_reader.get_car_number_by_color(car_color)

    def slot_numbers_for_cars_with_colour(self, car_color):
        self.__ticket_reader.get_slots_by_color(car_color)

    def slot_number_for_registration_number(self, car_number):
        self.__ticket_reader.get_slot_by_car_number(car_number)

    def status(self):
        """
        The method to show the parking status of the parking lot
        """

        print("\nSlot No.\t\tRegistration No\t\tColour")
        print("-"*50)

        for slot_id, ticket in self.__ticket_reader.get_allotted_tickets():
            level_id = ticket.get_level_id()
            allotted_slot = self.__levels[level_id - 1].get_slots()[slot_id]
            car_details = allotted_slot.get_car_details()
            car_color = car_details.get_car_color()
            car_number = car_details.get_car_number()
            print(str(slot_id) + "\t\t\t\t" + str(car_number) + "\t\t" + str(car_color))

    def get_total_number_of_levels(self):
        return self.__levelCount

    def get_total_number_of_slots(self):
        return self.__total_space_count

    def get_levels(self):
        return self.__levels
