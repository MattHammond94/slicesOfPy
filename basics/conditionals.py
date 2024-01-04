# Python is WHITESPACE DEPENDENT
# TWO SPACES WILL STILL RUN - However four is recomeneded as per PEP 8 style guides
# If statements are followed by a colon and then 4 spaces to execute as below:
# Only the first statement below will execute as the second does not evaluate to True

if len("CherryPy") > 5:
    print("Thats a long py")
    
if len("cabbagePy") > 20:
    print("Thats a small py")
    
# Must have a blank line between each new conditional.
# If elses appear as below and also require 4 spaces.

name = "tasty_lemon_py"
if len(name) > 25:
    print("That is a very long py")
    print(name)
else:
    print("Thats not a long name")
    print(name)
  
if isinstance(name, int) and name.isspace():
    print("This is a string thats not empty")
else:
    print("This is not a string")
    
if len(name) > 25:
    print("This is a long old name")
elif len(name) > 20:
    print("Quite long")
else:
    print("Short name")

# ^^^^ elsif is elif <<< wtf?
