'''
Adapt the code so that it assigns input into the 'name' variable. CHALLENGE - put a prompt in the input command to ask the user for their name. 
Combine lines 'Do you like programming' and answer = input so that it the input has a prompt in it.
Make the output on the next to last line include both the name and the answer variables.
Add comments to explain what you have changed.
'''
print("Hello, what is your name?")
name = input()
print("We want to know if you like programming!\n")
print(f"Do you like programming {name}?")
answer = input()

print(f"Great {name}! You said {answer}!") if answer == "Yes" else print("Bye")
print("Let's learn some Python today") if answer == "Yes" else print()
