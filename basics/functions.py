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

# Custom functions:

def greet(name):
    print(f"Hello, {name}!")

greet("BigMattyDon")

def seconds_in_weeks(weeks):
    return(weeks * 7 * 24 * 60 * 60)
  
print(seconds_in_weeks(2))


# Using functions as arguments:

def add(num1, num2):
    return num1 + num2

adder = add  # assigned the function to a variable

print(adder(1, 2))

# Defining multiple functions to pass as arguments

def calculate_tax_for_the_shire(grossPay):
    return grossPay * 0.2


def calculate_tax_for_mirkwood(grossPay):
    return grossPay * 0.9


def calculate_tax_for_mordor(grossPay):
    return grossPay * 0.9 + 500


def report_pay(gross_pay, calculate_tax):
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"


print("Frodo's Pay:")
print(report_pay(5000.0, calculate_tax_for_the_shire))
print("Bombadil's Pay:")
print(report_pay(4320.0, calculate_tax_for_mirkwood))
print("Mount Doom's Pay:")
print(report_pay(5000.0, calculate_tax_for_mordor))

# Weather report

def as_sun_lover(temp):
    if temp >= 25:
        return "great"
    else:
        return "not great"
    

def as_snow_lover(temp):
    if temp <= 0:
        return "great"
    else:
        return "not great"

def report_weather(temp, function):
    return function(temp)

print(report_weather(22, as_sun_lover))
print(report_weather(26, as_sun_lover))
print(report_weather(22, as_snow_lover))
print(report_weather(0, as_snow_lover))
