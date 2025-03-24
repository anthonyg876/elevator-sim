# elevator-sim
A simple elevator simulation that models basic elevator behavior and floor requests processing.

## Features
- Sets up the number of floors in a building
- Can request specific floors for the elevator to stop at.
- Elevator will move to all floors above the current floor before heading down to the floors below.

## Run this
```sh
python3 elevator.py
```

## Assumptions and Limitations
The elevator simulation makes several assumptions to focus on the moving of floors logic:
- No weight limit: The elevator doesn't account for total weight from passengers.
- Static requests: Once runElevator is called, the current list of requestedFloors gets processed. This can be improved with:
    - Running the runElevator method on a seperate thread.
    - Have a message queue listen for requests to update the requestedFloors.

