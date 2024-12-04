import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option_game = [rock, paper, scissors]

random_option = random.randint(0,2)

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if player_choose == 0:

    print(rock)

elif player_choose == 1:
    print(paper)

else:
    print(scissors)

print(f"computer choice: {option_game[random_option]}")

if player_choose == 0 and random_option == 0:
    print("It's a draw")
elif player_choose == 0 and  random_option == 1:
    print ("You Lose")
elif player_choose == 0 and random_option == 2:
    print("You win")

elif player_choose == 1 and random_option == 1:
    print("It's a draw")

elif player_choose == 1 and  random_option == 2:
    print ("You Lose")

elif player_choose == 1 and random_option == 0:
    print("You win")

elif player_choose == 2 and random_option == 2:
    print("It's a draw")

elif player_choose == 2 and  random_option == 0:
    print ("You Lose")

elif player_choose == 2 and random_option == 1:
    print("You win")



