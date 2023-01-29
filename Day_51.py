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

# Example-1

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

# snake_water_gun()



# Example-2
def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    return 1


comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if (score == 0):
    print("Its a draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")
