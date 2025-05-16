# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_left():
    print("Turn left")

def at_goal():
    print("At goal")

def wall_in_front():
    print("Wall inside front")

def front_is_clear():
    print("Front is clear")

def move():
    print("Move forward")

def wall_on_right():
    print("Wall on right")

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front():
        turn_right()
    elif front_is_clear():
        move()
        if wall_on_right():
            turn_left()
