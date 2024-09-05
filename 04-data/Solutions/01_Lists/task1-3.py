# Add comments to this code to explain how it works and predict what it will do.

usernames = [] # Create empty list to store usernames

while True: # Run the program until the user enters 'done'
    username = input("Please enter a username (write 'done' to stop)\n") # Ask for a new username
    if username == 'done': # Check if user entered done
        break # Stop the program
    if username in usernames: # Check if username already exists
        print("Sorry! This username is already taken.") # Inform the user that the name is already taken
        continue # Jump back to the top of the loop (line 5)
    usernames.append(username) # Add the new username to the list
    print('Success!')

print(usernames) # Print all usernames in the list