'''
Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import math
import turtle
cursor = turtle.Turtle()


def calc_distance(pen):
    initial_pos = [0, 0]
    while True:
        data = input(': ')
        if not data:
            break
        movement = data.split(' ')
        direction = movement[0]
        steps = int(movement[1])
        if direction == 'UP':
            initial_pos[1] += steps
            pen.left(90)
            pen.forward(initial_pos[1])
        elif direction == 'DOWN':
            initial_pos[1] -= steps
            pen.backward(initial_pos[1])
        elif direction == 'LEFT':
            initial_pos[0] -= steps
            pen.right(90)
            pen.forward(initial_pos[0])
        elif direction == 'RIGHT':
            initial_pos[0] += steps
            pen.backward(initial_pos[0])
        else:
            pass
    return initial_pos


current_position = calc_distance(cursor)
rel_dist = round(math.sqrt((current_position[0]**2 + current_position[1]**2)))
print(rel_dist)
turtle.done()
