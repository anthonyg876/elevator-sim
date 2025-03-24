from enum import Enum

class Direction(Enum):
    IDLE = 0
    UP = 1
    DOWN = 2

class Elevator:
    def __init__(self, floors: int):
        self.currentFloor = 0
        self.maxFloors = floors
        self.direction = Direction.IDLE
        self.requestedUpFloors = set()
        self.requestedDownFloors = set()

    def requestFloor(self, floor: int):
        """ Add a floor to the set of requested floors available"""
        if floor < 0 or floor > self.maxFloors:
            print("invalid floor requested, floor requested={floor}, accepted range: 0 : {self.maxFloors}")
            return
        if floor == self.currentFloor:
            print("currently on the {floor}th floor")
            return
        if floor > self.currentFloor:
            self.requestedUpFloors.add(floor)
            return
        if floor < self.currentFloor:
            self.requestedDownFloors.add(floor)
            
    

    def selectDirection(self):
        if not self.requestedFloors:
            self.direction = Direction.IDLE
            return
        
        

        

        
        


