'''
Adapt the code so that it assigns input into the 'name' variable. CHALLENGE - put a prompt in the input command to ask the user for their name. 
Combine lines 'Do you like programming' and answer = input so that it the input has a prompt in it.
Make the output on the next to last line include both the name and the answer variables.
Add comments to explain what you have changed.
'''

name = input('Name:\n>')
print("We want to know if you like programming!\n")
answer = input(f"Do you like programming {name}?\n>")
print(f"Great! You said {answer}!")
print("Let's learn some Python today")

