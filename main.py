#The purpose of this repo is to hold the solution for Reeborg's World Maze project

#This code is not intended to run here, but on the Reeborg's World site when working on the Maze challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
        
    else:
        turn_left()