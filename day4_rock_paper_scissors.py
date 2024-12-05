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

game_options = [rock, paper, scissors]

player_choise = int(input("Type 0 for Rock, 1 for paper and 2 for scissors: "))
if player_choise >=3 or player_choise < 0:
    print("Invalid Option")

print(game_options[player_choise])

computer_choise = random.randint(0,2)
print(game_options[computer_choise])

if player_choise >= 3 or player_choise < 0:
    print("You Lose, choose a valid option")

elif computer_choise == 0 and player_choise == 2:
    print("You Lose")

elif player_choise == 0 and computer_choise == 2:
    print("You Win")

elif player_choise > computer_choise:
    print("you Win")

elif computer_choise > player_choise:
    print("You Lose")

elif computer_choise == player_choise:
    print("It's a Draw")

