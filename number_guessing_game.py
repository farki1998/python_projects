number = [i for i in range(0,101)]
import random
is_continued = "y"
def play_game(numtime):
  for eachtime in range(0,numtime):
    status = "lose"
    which_number = int(input("What is the number you chose? "))
    if random_number>which_number:
      print("The number is higher")
    elif random_number<which_number:
      print("The number is lower")
    elif random_number == which_number:
      print("The number is correct. Congratulations you WIN")
      status = "win"
      break
  if status == "lose":
    print ("You lost")
while is_continued == "y":
  random_number = random.choice(number)
  easy_or_hard = input("Press easy or hard ")
  if easy_or_hard=="hard":
    play_game(5)
  elif easy_or_hard=="easy":
    play_game(10)
  is_continued = input("Do you want to continue? y or n?")
