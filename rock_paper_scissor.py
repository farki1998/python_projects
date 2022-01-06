#WELCOME TO A SIMPLE PYTHON GAME

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

#Write your code below this line 👇
import random
player_name = input("What is your name? ")
player_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
comp_play = ["Rock","Paper","Scissor"]
comp_rand = random.randint(0,2)
computer_final = comp_play[comp_rand]

if player_input == "0":
  print(f"{player_name} chose Rock")
  print(rock)
  if computer_final == "Rock":
    print("Computer chose Rock")
    print(rock)
    print("The result is draw")
  elif computer_final == "Scissor":
    print("Computer chose Scissor")
    print(scissors)
    print(f"{player_name} WON")
  elif computer_final == "Paper":
    print("Computer chose Paper")
    print(paper)
    print(f"{player_name} LOST, Computer WON")
elif player_input == "1":
  print(f"{player_name} chose Paper")
  print(paper)
  if computer_final == "Paper":
    print("Computer chose Paper")
    print(paper)
    print("The result is draw")
  elif computer_final == "Scissor":
    print("Computer chose Scissor")
    print(scissors)
    print(f"{player_name} LOST, Computer WON")
  elif computer_final == "Rock":
    print("Computer chose Rock")
    print(rock)
    print(f"{player_name} WON")
elif player_input == "2":
  print(f"{player_name} chose Scissor")
  print(scissors)
  if computer_final == "Paper":
    print("Computer chose Paper")
    print(paper)
    print(f"{player_name} WON")
  elif computer_final == "Scissor":
    print("Computer chose Scissor")
    print(scissors)
    print("The result is draw")
  elif computer_final == "Rock":
    print("Computer chose Rock")
    print(rock)
    print(f"{player_name} LOST, Computer WON")
