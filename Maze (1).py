def turn_right():
    turn_left()
    turn_left()
    turn_left()
def left_is_clear():
    turn_left()
    if not wall_in_front():
        turn_right()
        return 1
    else:
        turn_right()
        return 0
def turn_around():
    turn_left()
    turn_left()
def condition():
    if right_is_clear():
        turn_right()
    elif left_is_clear():
        turn_left()
    elif not right_is_clear() and left_is_clear()==0 and wall_in_front():
        turn_around()
    if left_is_clear() and right_is_clear() and not wall_in_front():
        move()
while not at_goal():
    if not wall_in_front():
        move()
        condition()
    else:
        condition()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
