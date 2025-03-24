from enum import Enum

class Direction(Enum):
    IDLE = 0
    UP = 1
    DOWN = 2

class Elevator:
    def __init__(self, floors: int):
        self.currentFloor = 1
        self.maxFloors = floors
        self.direction = Direction.IDLE
        self.requestedFloors = set()


