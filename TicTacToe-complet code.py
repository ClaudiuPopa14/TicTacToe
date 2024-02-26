board = [' ']*10 

def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']

   
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1:Vrei sa fii X sau 0? ').upper()

    if marker == 'O':
        
        return ('X', 'O')
    else:
        return ('O', 'X')
        

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,marker) :
    return ((board[7] == marker and board[5] == marker and board[3] == marker)or
            (board[4] == marker and board[5] == marker and board[6] == marker)or
            (board[1] == marker and board[2] == marker and board[3] == marker)or
            (board[7] == marker and board[4] == marker and board[1] == marker) or 
            (board[8] == marker and board[5] == marker and board[2] == marker) or  
            (board[9] == marker and board[6] == marker and board[3] == marker) or  
            (board[7] == marker and board[5] == marker and board[3] == marker) or 
            (board[9] == marker and board[5] == marker and board[1] == marker)) 

win_check(test_board,'X')
import random
def choose_first():
    if random.randint(0,1) == 0 :
        return 'Player2'
    else :
        return 'Player1'
    
def space_check(board,position):
    return board[position] == ''

def board_full (board) :
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True  

def player_choise(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Alege pozitia urmatoare (1-9) '))
    return position

def replay():
    return input ('Joci again? Enter Yes or No: ').lower().startswith('y')


print ('Bine ai venit la x si 0')

while True :
    theboard = [''] *10
    player1_marker,player2_marker = player_input()
    turn=choose_first()
    print( turn+'e primul ')
    play_game = input (' Gata de joc? Tasteaza yes or no:  ')
    if play_game.lower()[0] == 'y' :
        game_on = True
    else:
        game_on = False 
    while game_on:
        if turn == 'Player1':

            display_board(theboard)
            position = player_choise(theboard)
            place_marker(theboard,player1_marker,position)

            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('Congrats, ai castigat')
                game_on = False
            else:
                if board_full(theboard):
                    display_board(theboard)
                    print('Egal')
                    break
                else:
                    turn = 'Player2'
        else:
            display_board(theboard)
            position = player_choise(theboard)
            place_marker(theboard,player2_marker,position) 
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print('Congrats, ai castigat')
                game_on = False
            else:
                if board_full(theboard):
                    display_board(theboard)
                    print('Egal')
                    break
                else:
                    turn = 'Player1'
    if not replay():
        break
            
        

            
        
