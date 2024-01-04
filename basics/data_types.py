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
