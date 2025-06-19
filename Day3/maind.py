print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("Where do you want to go? Left or Right. \n").lower()
if left_or_right == "left":
    print("You come to a river. Swim or wait for a boat?")
    swim_or_wait = input(" Please type \"swim\" or \"wait\". \n").lower()
    if swim_or_wait == "wait":
        print("You come to three doors. Which one would you open?")
        doors = input("Red, blue, or yellow? \n").lower()
        if doors == "yellow":
            print("You find the treasure. You win!")
        elif doors == "red":
            print("The room behind the door is filled with fire. You get burned. Game over.")
        elif doors == "blue":
            print("The room behind the door is full of beasts. You get eaten. Game over.")
        else:
            print("You type something wrong. Game over.")
    else:
        print("You get attacked by a trout. Game over.")
else:
    print("You fall into a hole. Game Over.")
