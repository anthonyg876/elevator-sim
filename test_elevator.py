import unittest

from elevator import Elevator, Direction

class TestElevator(unittest.TestCase):

    def setUp(self):
        self.elevator = Elevator(10)

    def test_init(self):
        self.assertEqual(self.elevator.currentFloor, 0)
        self.assertEqual(self.elevator.direction, Direction.IDLE)
        self.assertEqual(self.elevator.maxFloors, 10)
        self.assertEqual(self.elevator.requestedDownFloors, set())
        self.assertEqual(self.elevator.requestedUpFloors, set())




if __name__ == '__main__':
    unittest.main()
