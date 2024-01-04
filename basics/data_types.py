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
name = "Matt"
favourite_py = "Chocolate"
print('Hello my name is %s! My favourite py is: %s,'%(name, favourite_py))

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

# Classes in Python:
# class methods in Python require self to be passed as the first argument otherwise will error.
class Greeter():
    def hello(self):
        return "Hello!"
  
    def good_bye(self):
        return "Good bye!"

greeter = Greeter()
print(greeter.good_bye())