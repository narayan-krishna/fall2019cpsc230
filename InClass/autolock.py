engine = input("is the engine still running ")
gear = input("is the car in parking gear ")
lights = input("are the lights on ")
doors = input("are all the doors closed ")

locked = 0

if engine == 'n':
    locked += 1
else:
    print("engine is still running")

if gear == 'y':
    locked += 1
else:
    print("car is not in parking gear")

if lights == 'n':
    locked += 1
else:
    print("lights are on")

if doors == 'y':
    locked += 1
else:
    print("doors must be closed")

if locked == 4:
    print("car is locked!")
