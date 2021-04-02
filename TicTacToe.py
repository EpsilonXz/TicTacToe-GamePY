Winner = False
Board = {
    'top_L':" ", 'top_M':" ", 'top_R': " ", 
    'mid_L':" ", 'mid_M':" ", 'mid_R': " ",
    'bottom_L':" ", 'bottom_M':" ", 'bottom_R': " "
}

def PrintBoard(board):
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print('-+-+-')
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print('-+-+-')
    print(board['bottom_L'] + '|' + board['bottom_M'] + '|' + board['bottom_R'])
turn = 'X'
def PlayGame(Board):
    global Winner
    Moves = []
    print('the places you can move to are: top_L, top_M, top_R, mid_L, mid_M, mid_R, bottom_L, bottom_M, bottom_R')
    for i in range(9):
        global turn
        PrintBoard(Board)
        print(f'Playing now {turn}')
        move = input('Where do you want to move?')
        if move in Moves or move not in Board:
            while True:
                move = input('Try again... Where do you want to move?')
                if move in Moves or move not in Board:
                    continue
                else:
                    break
        Moves.append(move)
        Board[move] = turn
        if Board['top_L'] == Board['top_M'] == Board['top_R'] == turn:
            Winner = True
            break
        elif Board['mid_L'] == Board['mid_M'] == Board['mid_R'] == turn:
            Winner = True
            break
        elif Board['bottom_L'] == Board['bottom_M'] == Board['bottom_R'] == turn:
            Winner = True
            break
        elif Board['top_L'] == Board['mid_M'] == Board['bottom_R'] == turn:
            Winner = True
            break
        elif Board['top_R'] == Board['mid_M'] == Board['bottom_L'] == turn:
            Winner = True
            break
        elif Board['top_L'] == Board['mid_L'] == Board['bottom_L'] == turn:
            Winner = True
            break
        elif Board['top_M'] == Board['mid_M'] == Board['bottom_M'] == turn:
            Winner = True
            break
        elif  Board['top_R'] == Board['mid_R'] == Board['bottom_R'] == turn:
            Winner = True
            break
        if turn == 'X': turn = 'O'
        elif turn == 'O': turn = 'X'

    PrintBoard(Board)
PlayGame(Board)
while True:
    if Winner == False:
        PlayAgain = input('Tie do you want to play again? type Y/n')
        if PlayAgain == 'Y':
            Board = {
                'top_L':" ", 'top_M':" ", 'top_R': " ", 
                'mid_L':" ", 'mid_M':" ", 'mid_R': " ",
                'bottom_L':" ", 'bottom_M':" ", 'bottom_R': " "
            }
            PlayGame(Board)
        else:
            print('Have a nice day!')
            break
    else:
        print(f'{turn} wins! Do you want to play again? type Y/n')
        PlayAgain = input()
        if PlayAgain == 'Y':
            Board = {
                'top_L':" ", 'top_M':" ", 'top_R': " ", 
                'mid_L':" ", 'mid_M':" ", 'mid_R': " ",
                'bottom_L':" ", 'bottom_M':" ", 'bottom_R': " "
            }
            Winner = False
            PlayGame(Board)
        else:
            print('Have a nice day!')
            break

"""
possible combinations: 
    order LTR, RTL:
    ¬Board['top_L'] == Board['top_M'] == Board['top_R']
    ¬Board['mid_L'] == Board['mid_M'] == Board['mid_R']
    ¬Board['bottom_L'] == Board['bottom_M'] == Board['bottom_R']
    diagnal:
    ¬Board['top_L'] == Board['mid_M'] == Board['bottom_R']
    ¬Board['top_R'] == Board['mid_M'] == Board['bottom_L']
    up, down:
    ¬Board['top_L'] == Board['mid_L'] == Board['bottom_L']
    ¬Board['top_M'] == Board['mid_M'] == Board['bottom_M']
    ¬Board['top_R'] == Board['mid_R'] == Board['bottom_R']
"""
