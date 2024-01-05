# Strings:
py_4 = "   P0r K "

# String manipulation is the same:
print(py_4[3])
print(py_4[-5])

# Slice notation (Uses and start and stop index value):
sentence = "This is a sentance about pys"

#If I only want the word "This"
print(sentence[0:4])

#String interpolation:
selected_word = sentence[10:18]
print(f"A different {selected_word}")

# Using %
my_name = "Matt"
favourite_py = "Chocolate"
print('Hello my name is %s! My favourite py is: %s,'%(my_name, favourite_py))

# Uses integers and float values:
print(2.5.is_integer())  # Returns False
print("   ".isspace())   # Returns True
print(float(2))
print(float(4 + 4))
print(int(2.8 + 2.3))
print(int(2.2 + 2.1))

# Booleans are capitalized:
boo_py_1 = True
boo_py_2 = False

# Boolean logical operators are keywords as opposed to pipes(||) etc
print(1 == 1)
print(2 == 4)
print(True and False)
print(True or False)
print(not True)
print(not False)
print(len("cabbage") > 3 and len("suede") > 13)

# Using Ternarys in Python:
x, y = 44, 440
print("Yes it is" if x > y else "No it is not")

# Lists (Arrays):
films = ["The Thing", "Sexy Beast", "Akira"]
films.append("Blade")
print(films)
films.sort()
print(films)
print(films.pop(1))
films.reverse()
print(films)
print(films.index("The Thing"))
print(films.clear())
print(films)

# Advanced lists (iterables):
py_chart = ["ApplePy", "CherryPy", "ZebraPy"]
interator_py_chart = iter(py_chart)

# using next:
iterable_list = iter(["ApplePy", "CherryPy", "ZebraPy"])
x = next(iterable_list)
print(x)

x_2 = next(iterable_list)
print(x_2)

x_3 = next(iterable_list)
print(x_3)

# filter similar to JS - filter takes two args: a function (in the case below "is_acebook" function) and a list.
# filter returns an iterable however. next allows us to grab the first element from the iterable which in this scenario would only be 1 item.
passwords = [
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

def is_acebook(password):
    return password['service'] == 'acebook'

print(next(filter(is_acebook, passwords)))

# map, like filter takes a function and a list.
result = map(lambda number: number * 2, [1, 2, 3, 4])
print(list(result))


# Using LAMBDAS:
# lambdas are small functions with no names - lambda functions take a single argument in this case password:
print(next(filter(lambda password: password["service"] == "acebook", passwords)))


# List comprehensions:
# returns a list 
print([password for password in passwords if password['service'] == 'acebook'])
print([x for x in passwords if x['service'] == 'acebook'][0])

def are_passwords_long_enough(passwords):
    return len([x for x in passwords if len(x['password']) > 8]) == 0

print(are_passwords_long_enough(passwords))

# Using a list comprehension over using the map function:
print([number * 2 for number in [1, 2, 3, 4]])


# Dictionaries (JS objects or Hashes)
py_king = {
    "name": "Guido Van Rossum",
    "nationaility": "Dutch",
    "favourite_programming_language": "Python",
    "slices_of_py": ["Cherry", "Apple", "Shepherds"],
    "age": 108
}

print(py_king["name"])
print(py_king["age"])
print(py_king["slices_of_py"][0])
py_king["favourite_snake"] = "Black Mamba"
py_king["height"] = 6.2

print(py_king.keys())
print(py_king.values())
print(py_king.get("favourite_snake"))


# Advanced Dictionaries:

# Using comprehension within a dictionary
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

person = { "Name": "MatTyBoi", "Age": 44, "height": 5.10 }
for item in person:
    print(f"key value pair: {item} -> {person[item]}")


friends = ["Will", "Bernie", "Garth", "Suze"]
card_suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
from random import shuffle
shuffle(card_suit)
card_friends = {friend:card for (friend, card) in zip(friends, card_suit)}
print(card_friends)

players = { "Matt": 20, "Guido": 10, "Van-Dijk": 10 }
new_player = { "Some_dude": 0 }
players.update(new_player)
print(players)

# Next round using a loop:
next_round = {}
print(players.items())
for player, score in players.items():
    if score > 10:
        next_round[player] = score
        
print(next_round)

# Next round using filter:
next_round_2 = dict(filter(lambda player: player[1] < 20, players.items()))
print(next_round_2)

# Next round using dictionary comprehension:
next_round_3 = { key:value for (key, value) in players.items() if value > 10 }
print(next_round_3)

# Classes in Python:
# class methods in Python require self to be passed as the first argument otherwise will error.
class Person():
    def __init__(self, name, birthday, nationality):
        self.name = name
        self.birthday = birthday
        self.nationality = nationality
        
    def say_name(self):
        return self.name
        
    def hello(self):
        return "Hello!"
  
    def good_bye(self):
        return "Good bye!"

greeter = Person("MattyMoo", 14, "Irish")
print(greeter)
print(greeter.good_bye())
print(greeter.say_name())

# Can just directly call the initialized variables as below:
print(greeter.birthday)
