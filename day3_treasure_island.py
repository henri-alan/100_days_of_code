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

direction = input("Select your direction: right or left? ")
if direction == "left":
        print("You've com to a lake. There is an island in the middle of the lake")
        boat_or_swim = input('Type "wait" to wait for a boat. Or type "swim" to swim across.')
        if boat_or_swim == "wait":
            print(
                "You arrive at the island. There is a house with 3 doors.\n red, yellow and blue.")
            select_door = input("Which color do you choose?")
            if select_door == "red":
                print("game over, you're burned by fire.")
            elif select_door == "blue":
                print("Eaten by beasts. Game Over")
            elif select_door == "yellow":
                print("You Win!")
            else:
                print("Game Over.")
        else:
            print("Attacked by trout. Game Over")

else:
        print("End game, you fall in a hole")











