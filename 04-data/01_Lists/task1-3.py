# Add comments to this code to explain how it works and predict what it will do.

usernames = []

while True:
    username = input("Please enter a username (write 'done' to stop)\n")
    if username == 'done':
        break
    if username in usernames:
        print("Sorry! This username is already taken.")
        continue
    usernames.append(username)
    print('Success!')

print(usernames)
