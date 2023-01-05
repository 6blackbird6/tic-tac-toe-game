board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
current_player = 'X'
winner = None
game_ruinning = True

# printing the game board
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('__________')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('__________')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# take a player input
def player_input():
    player_input = int(input('Enter a number from 1 to 9: '))
    if player_input in range(1, 10) and board[player_input-1] == '-':
       board[player_input-1] = current_player 
    else:
        print('Oops... this square is already filled!')
# check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
       winner = board[1] 
       return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != '-':
        winner = board[7]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != '-':
       winner = board[3] 
       return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[5]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != '-':
       winner = board[4] 
       return True
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[4]
        return True

def check_tie(board):
    global game_ruinning
    if board.count('-') == 0:
        print_board(board)
        print('It\'s a tie!')
        game_ruinning = False
# switch the player
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def check_win():
    global game_ruinning
    if check_diagonal(board) or check_horizontal(board) or check_row(board):
        print_board(board)
        print(f'The winner is {winner}')
        game_ruinning = False

# check for win or tie again
while game_ruinning:
    print_board(board)
    player_input()
    check_win()
    check_tie(board)
    switch_player()