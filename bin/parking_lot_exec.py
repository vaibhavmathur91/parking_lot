import os
from class_parkinglot import ParkingLot


def parse_input(pl_instance, args):
    arg_list = args.split()
    number_of_args = len(arg_list)
    if number_of_args == 0:
        return
    function_name = arg_list[0].strip()
    try:
        if number_of_args == 1:
            getattr(pl_instance, function_name)()
        elif number_of_args == 2:
            getattr(pl_instance, function_name)(arg_list[1])
        else:
            getattr(pl_instance, function_name)(arg_list[1:])
    except Exception as error:
        print("Not a valid method :: ", error)


def initiate_parking_lot(arguments):
    argument_list = arguments.split()
    try:
        """
        -- check if correct condition ?
        >> if argument_list[0] == create_parking_lot:
        """
        parking_lot_object = ParkingLot(int(argument_list[1]))
    except Exception as error:
        print("No Parking Lot found :: ", error)
        exit(-1)
    return parking_lot_object


def driver(pl_instance, file_obj):
    for line in file_obj:
        if not pl_instance:
            pl_instance = initiate_parking_lot(line)
        else:
            parse_input(pl_instance, line)


def main():
    try:
        pl_instance = None
        file_name = "file_input.txt"
        with open(os.path.join("input", file_name)) as file_obj:
            driver(pl_instance, file_obj)
    except Exception as error:
        print("No File Found :: ", error)
        """
        -- check if No File condition ?
        >> take input() from user ?
        """


if __name__ == "__main__":
    main()
