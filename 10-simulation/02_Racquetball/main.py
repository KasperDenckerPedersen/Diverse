import random

def print_intro():
    print("Welcome to the Racquetball simulator!\nThis game simulates the outcome of n number of games")

def get_inputs():
    n = int(input("How many games should be played?\n>"))
    print("What is the win probability of the players when serving (Between 0-1): ")
    probA = float(input("Player A: "))
    probB = float(input("Player B: "))
    return n, probA, probB

def sim_n_games(n, probA, probB):
    WinsA = 0
    WinsB = 0
    for i in range(n):
        scoreA, scoreB = sim_one_game(probA, probB)
        if scoreA > scoreB:
            WinsA += 1
        else:
            WinsB += 1
    return WinsA, WinsB

def sim_one_game(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = random.choice(['playerA', 'playerB'])
    while scoreA < 15 and scoreB < 15:
        if serving == 'playerA':
            if random.random() <= probA:
                scoreA += 1
            else:
                serving = 'playerB'
        else:
            if random.random() <= probB:
                scoreB += 1
            else:
                serving = 'playerA'
    return scoreA, scoreB

def print_summary(WinsA, WinsB):
    games = WinsA + WinsB
    shareA = WinsA / games
    shareB = WinsB / games
    print('Summary of the simulation')
    print(f'Total number of games played: {games}\nPlayer A: {WinsA} | {shareA}\nPlayer B: {WinsB} | {shareB}')
    return

print_intro()
n, probA, probB = get_inputs()
WinsA, WinsB = sim_n_games(n, probA, probB)
print_summary(WinsA, WinsB)
