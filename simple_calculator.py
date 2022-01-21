logo = """
Welcome to my simple calculator
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""
print(logo)

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n1
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
command = {"+":add,
"-":subtract,
"*":multiply,
"/":divide}
numb1 = float(input("What is the first num? "))
numb2 = float(input("What is the second number? "))
for key in command:
  print(key)
operations = input("What is the operation? ")
calculation_function = command[operations]
answer = calculation_function(numb1,numb2)
print(f"{numb1}{operations}{numb2}={answer}")
