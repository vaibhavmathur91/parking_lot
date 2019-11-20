import unittest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from bin.class_parkinglot import ParkingLot


class TestParkingLot(unittest.TestCase):

    @classmethod
    def set_parking(cls):
        # Slots are variable based on user input
        cls.slots_per_level = 5
        # Levels are predefined for this project = 1
        cls.total_level = 1
        cls.parking = ParkingLot(cls.slots_per_level)

    def test_to_create_parking_lot(self):
        self.set_parking()
        self.assertEqual(self.parking.get_total_number_of_slots(), self.slots_per_level, msg="Mismatch Slots")
        self.assertEqual(self.parking.get_total_number_of_levels(), 1, msg="Mismatch Levels")

    def test_to_success_park_car(self):
        reg_no = "KA-01-HH-1234"
        color = "White"
        slot_id = self.parking.park([reg_no, color])
        allotted_slot = self.parking.get_levels()[self.total_level - 1].get_slots()[slot_id]
        self.assertTrue(allotted_slot.is_car_parked(), "Park failed.")

    def test_to_error_park_car(self):
        allotted_slot = self.parking.get_levels()[self.total_level - 1].get_slots()[self.slots_per_level]
        self.assertFalse(allotted_slot.is_car_parked(), "Park failed.")


if __name__ == '__main__':
    unittest.main()
