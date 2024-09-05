def add_five(number):
  result = number + 5
  return result

number = 10

print(add_five(number))

result = add_five(number) # To fix the code we have to add this line

print(result)

# What will be the outputs of the program?
  # The program will print 15 and result in an error afterwards

# Explain why the code will fail and fix the issue it
  # The code will fail as result is only a local variable in the scope of the function add_five and does not exist in the global scope. To fix it we have to assigned the returned value to a new variable
