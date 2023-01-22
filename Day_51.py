"""
Snake Water Gun
----------------
Snake, Water and Gun == a variation of the children's game "rock-paper-sc==sors" where players use hand gestures
to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.
Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI.
Use proper functions to check for win.


#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D


"""


import random


def snake_water_gun():
    userInput = int(input("Enter any number between 0 to 2: "))
    print(type(userInput))
    # snake,water,gun = 0,1,2
    randomNum = round(random.uniform(0, 2))
    if userInput == randomNum:
        print("It's a Tie")
    if userInput == 0 and randomNum == 1:
        print("It's water. You won")
    if userInput == 0 and randomNum == 2:
        print("It's Gun. You lost")
    if userInput == 1 and randomNum == 0:
        print("It's Snake. You lost")
    if userInput == 1 and randomNum == 2:
        print("It's Gun. You Won")
    if userInput == 2 and randomNum == 0:
        print("It's Gun. You Won")
    if userInput == 2 and randomNum == 1:
        print("It's water. You lost")

snake_water_gun()
