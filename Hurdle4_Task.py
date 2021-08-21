def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def jump_high():
    turn_left()
    move()
    turn_right()


def down():
    move()
    turn_right()


while not at_goal():
    while not wall_on_right():
        turn_right()
        move()
    if wall_in_front() and not right_is_clear():
        turn_left()
    if wall_on_right() and wall_in_front():
        jump_high()
        if front_is_clear():
            down()
    if not front_is_clear():
        turn_left()
    else:
        move()