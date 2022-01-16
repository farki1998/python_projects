#Step 1

word_list = ["laptop", "mouse", "keyboard","tablet","storage"]
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
  display.append("_")
end_game = False
while not end_game:
  guess = input("Guess a letter ").lower()
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
  if guess not in chosen_word:
    lives = lives-1
  print(display)
  if "_" not in display:
    end_game = True
    print("you win")
  if lives == 0:
    end_game = True
    print("You Lose")
  print(stages[lives])
