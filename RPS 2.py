import random
symbols = ['rock', 'paper', 'scissors']
player_wins = 0
computer_wins = 0
while max([player_wins, computer_wins])<3:
    player_symbol = None
    while player_symbol is None:
        input_symbol = input("What symbol do you want? ")
        if input_symbol in symbols:
            player_symbol = input_symbol
        else:
            print('Please rock paper or scissors')

    computer_symbol = random.choice(symbols)
    
    print('player:', player_symbol)
    print('computer:', computer_symbol)
    if player_symbol == computer_symbol:
        print('TIE')
    elif player_symobl == 'rock':
        if computer_symbol == 'paper':
            print ('Computer Wins')
            computer_wins += 1
        else:
            print('Player Wins')
            player_wins += 1
            
    elif player_symobl == 'paper':
        if computer_symbol == 'scissors':
            print ('Computer Wins')
            computer_wins += 1
        else:
            print('Player Wins')
            player_wins += 1
            
    elif player_symobl == 'scissors':
        if computer_symbol == 'rock':
            print('Computer Wins')
            print('computer_wins += 1')
        else:
             print('Player Wins')
             player_wins += 1
