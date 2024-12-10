def turn_right():
    turn_left()
    turn_left()
    turn_left()
def one_lap():
    while wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        while not wall_in_front():
            move()
        else:
            turn_left()
while  not at_goal():
    if not wall_in_front():
        move()
    else:
        turn_left()
        one_lap()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
