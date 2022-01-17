alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text_type,shiftamount):
  message = ""
  for letter in text_type:
    position = alphabet.index(letter)
    new_position = position+shiftamount
    message += alphabet[new_position]
  print(message)
def decrypt(text_type,shiftamount):
  message = ""
  for letter in text_type:
    position = alphabet.index(letter)
    new_position = position-shiftamount
    message += alphabet[new_position]
  print(message)
if direction=="encode":
  encrypt(text_type=text,shiftamount=shift)
elif direction=="decode":
  decrypt(text_type=text,shiftamount=shift)
else:
  print("Please type in either encode or decode")
