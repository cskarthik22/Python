'''

#1: Print the board
#2: Assign Markers to Players
#3: Choose Player to start
#4: Choose a postion on the board to mark
    a) Space check
    b) full board check
    c) check for win
#5: Ask for next players postion 
#6: Run the Game

'''
import os
import random

os.system('clear') 

#1: Print the board
def display_board(board):
    print(' ' + ' | ' + ' ' + ' | ' + ' ' )
    print(board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print(' ' + ' | ' + ' ' + ' | ' + ' ' )
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print(' ' + ' | ' + ' ' + ' | ' + ' ' )
    print(board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print(' ' + ' | ' + ' ' + ' | ' + ' ' )

#2: Assign Markers to Players
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = raw_input('Player1: Choose X or O: ').upper()
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
        

#3: Choose Player to start
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'PLAYER-01'
    else:
        return 'PLAYER-02'
    
#4: Choose a postion on the board to mark
def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, postion):
        position = int(input('choose a position 1-9: '))
    return position

def place_marker(board,marker,position):
    board[position] = marker

#4.a: Space Check
def space_check(board, position):
    if board[position]==' ':
        return True

#4.b Fullboard Check
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#5: Check for win
def check_win(board,player):
    if (   (board[1]==board[2]==board[3]==player) 
        or (board[4]==board[5]==board[5]==player) 
        or (board[7]==board[8]==board[9]==player) 
        or (board[1]==board[4]==board[7]==player)  
        or (board[2]==board[5]==board[8]==player) 
        or (board[3]==board[5]==board[9]==player) 
        or (board[1]==board[5]==board[9]==player) 
        or (board[3]==board[5]==board[7]==player)  ):
        return True
    else:
        return False

def replay():
    choice = input('Play again? Yes or No')
    return choice == 'Yes'

#================================================
#6 Run the Game
def run():
    print(' Welcome to tic-tac-toe !!!')
    while True:
        # setup 
        game_board = [' ']*10
        player1_marker,player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first...')

        play_game = input('Ready to play? y or n? ')
        if play_game == 'y':
            game-on = True
        else:
            game_on = False

        while game_on:
            # Player01 turn
            if turn == 'PLAYER-01':
                display_board(game_board)
                pos = player_choice(game_board)
                place_marker(game_board,player1_marker,pos)
                if( win_check(board, player1_marker)):
                    display_board(game_board)
                    print('PLAYER01 has won the game !!')
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('Game tie...')
                        game_on = False
                    else:
                        turn = 'PLAYER-02'
            else:
                # Player02 turn
                if turn == 'PLAYER-02':
                    display_board(game_board)
                    pos = player_choice(game_board)
                    place_marker(game_board,player2_marker,pos)
                    if( win_check(board, player2_marker)):
                        display_board(game_board)
                        print('PLAYER02 has won the game !!')
                        game_on = False
                    else:
                        if full_board_check(game_board):
                           display_board(game_board)
                           print('Game tie...')
                           game_on = False
                        else:
                           turn = 'PLAYER-01'
                
         
        if not replay():
            break




testboard = ['#','X','O','X','O','X','O','X','O','X']
display_board(testboard)
player1_marker, player2_marker = player_input()
print("Player1 : " + player1_marker )
print("Player2 : " + player2_marker )

