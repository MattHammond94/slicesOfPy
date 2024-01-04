# Loops in Python

# For loops:
for i in range(5):
    print('Hello World')
    
for number in range(10):
    print(number)
    
num = 10
for i in range(5):
    num = num + 5
    print(num)
    
# Range can be used as range(start_at, stop_before, step_by)
# The below will print the ten times table up to 90 and stop.
for i in range(10, 100, 10):
    print(i)
    
# Looping through a string:    
name = "CherryPyPaul"
for i in name:
  print("Give me a " + i)
  
# While loops:
from random import randint
fav_number = 44
guess_correct = False

while not guess_correct:
    print("Guess my favourite number?")
    guess = randint(0, 50)
    if guess == fav_number:
        print("Correct! my favourite number is 44")
        guess_correct = True
    else: 
        print(f"{guess} is wrong! Try again!")
        