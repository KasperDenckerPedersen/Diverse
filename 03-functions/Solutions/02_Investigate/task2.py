def greet(name, msg="Good morning!"):
    print(f'Hi {name}, {msg}')

greet("Hans") # Hi Hans, Good morning!

greet("Hans", "How are you?") # Hi Hans, How are you?

greet("Good afternoon", "Hans") # Hi Good afternoon, Hans

greet("How are you?") # Hi How are you?, Good morning!

greet(msg="Good afternoon", name="Hans") # Hi Hans, Good afternoon

greet(name="Hans") # Hi Hans, Good morning!

greet(msg="Good afternoon") # Error as the required argument name is not parsed to the function

# What will be the outputs of the program?
    # See above

# How many custom functions are there in the code?
    # 1 (greet)

# How often is each of the custom functions called?
    # 7
