'''
Modify the code to build a program that allows a user to chose between different options. 
Option 1 should show all the available video games in the list. 
Option 2 should allow the user to enter the name of a video game and add it to the list if it is not already there. 
Option 3 should allow the user to enter the index of a game and delete it
Option 4 should stop the program
'''

def get_choice():
    print()
    print('1. Show games')
    print('2. Add game')
    print('3. Delete game')
    print('4. Shutdown')
    choice = int(input('>'))
    return choice

def show_games(games):
    for index in range(len(games)):
        game = games[index]
        print(f'{index}: {game}')

def add_game(games):
    game = input("Game: ")
    if game in games:
        print('You already have this game')
    else:
        games.append(game)
    return games

def delete_game(games):
    index = int(input('Index of the game to remove: '))
    games.pop(index)
    return games

videoGames = ["Mario", "Sonic", "Joust", "Zelda"]

while True:
    choice = get_choice()
    if choice == 1:
        show_games(videoGames)
    elif choice == 2:
        videoGames = add_game(videoGames)
    elif choice == 3:
        videoGames = delete_game(videoGames)
    elif choice == 4:
        break
    else:
        print('Invalid choice')