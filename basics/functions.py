# Similar built in functions:
print(str(67))
print(int('67'))
print(abs(-28))  # abs returns an integer as a positive value.
print(abs(22))
print(abs(0))
print(abs(-25))
print(len("Show me the length of this very long string please kind sir"))

# Similar to JS if a function is not explicitly called using parenthesis then the function itself is returned.
print(len)

# type returns the data type of its argument
print(type("A stringy string"))
print(type(444))
print(type(abs))

# Assigning variables and passing to functions:
word = "Chosen word"
word_length = len(word)
word_length_as_string = str(word_length)
print(word_length_as_string)

# methods differ to functions as they belong to a specific data types(can only be called on instances of certain objects.)
py_1 = "cherry"
py_2 = "keylime"
py_3 = "LEMONMERINGUE"
py_4 = "   P0r K "

print(py_1.capitalize())
print(py_2.upper())
print(py_3.lower())
print(py_4.isascii())  # returns true if all chars are ascii
print(py_4.isalpha())  # returns true if all chars are alphabet letters
print(py_4.strip())
print(py_4.strip().upper())

# String manipulation is the same:
print(py_4[3])
print(py_4[-5])

# Slice notation (Uses and start and stop index value):
sentence = "This is a sentance about pys"

#If I only want the word "This"
print(sentence[0:4])
