from enum import Enum
import time

class Direction(Enum):
    IDLE = 0
    UP = 1
    DOWN = 2

class Elevator:
    def __init__(self, floors: int):
        self.currentFloor = 0
        self.maxFloors = floors
        self.direction = Direction.IDLE
        self.requestedFloors = set()
        self.moving = False

    def requestFloor(self, floor: int):
        """ Add a floor to the set of requested floors available"""
        if floor < 0 or floor > self.maxFloors:
            print(f"invalid floor requested, floor requested={floor}, accepted range: 0 : {self.maxFloors}")
            return
        if floor == self.currentFloor:
            print(f"currently on the {floor}th floor")
            return
        print(f"{floor}th floor requested")
        if floor in self.requestedFloors:
            print(f"{floor}th floor has already been selected")
        
        self.requestedFloors.add(floor)
            
    def selectDirection(self) -> Direction:
        if not self.requestedFloors:
            self.direction = Direction.IDLE
            return Direction.IDLE
        for floor in self.requestedFloors:
            if floor > self.currentFloor:
                self.direction = Direction.UP
                return Direction.UP
            
        self.direction = Direction.DOWN
        return Direction.DOWN
            
        
    def move(self):
        if self.direction == Direction.UP:
            self.currentFloor += 1
        elif self.direction == Direction.DOWN:
            self.currentFloor -= 1
        currFloor = self.currentFloor
        print(f"Elevator moving to {currFloor}th floor")
        time.sleep(2)
    
    def runElevator(self):
        direction = self.selectDirection()
        if direction is Direction.IDLE:
            print("no floors were requested")
            return

        while self.requestedFloors:
            if self.currentFloor in self.requestedFloors:
                print(f"stopping at {self.currentFloor}th floor")
                self.requestedFloors.remove(self.currentFloor)
                time.sleep(2)
            
            if not self.requestedFloors:
                break
            
            self.move()

            self.selectDirection()

        print("all floors have been served")
        
        


elevator = Elevator(10)
elevator.currentFloor = 3
elevator.requestFloor(2)
elevator.requestFloor(5)
elevator.runElevator()

        
        

        

        
        


