def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

start_engine()

destination = input("where do you want to go? ")

if destination in ['library','techpark','hospital', 'mall', 'airport', 'university', 'stadium']:
    move_forward()
    if destination == "tech park":
        turn("right")
    elif destination == "library":
        turn("left")
    elif destination == 'hospital':
        follow_roundabout("first")
    elif destination == 'mall':
        follow_roundabout("second")
        move_forward()
        turn("right")
    elif destination == 'airport':
        follow_roundabout("third")
    elif destination == 'university' or 'stadium':
        follow_roundabout("fourth")
        move_forward
        if destination == 'university':
            turn("left")
        if destination == 'stadium':
            turn("right")
    print("you have arrived")
else:
    print("wrong destination")
    stop_engine()


