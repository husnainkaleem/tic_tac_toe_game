from random import random
import random


def board(game_input):
    print(game_input[7]+'|'+game_input[8]+'|'+game_input[9])
    print(game_input[4]+'|'+game_input[5]+'|'+game_input[6])
    print(game_input[1]+'|'+game_input[2]+'|'+game_input[3])

 # board(game_input)
def player_input():
    marker=''
    while marker !='X' and marker != 'O':
              marker=input('player1:please choose your marker')
    if marker == 'X':
              return ('X','O')
    else:
              return ('O','X')

#player_input()

#player1,player2=player_input()
#print(player1)
#print(player2)

def put_marker(game_input,marker,position,):
    game_input[position]=marker
   # board(game_input)

def win(game_input,marker):
    return ((game_input[1]==game_input[2]==game_input[3]==marker) or
        (game_input[4]==game_input[5]==game_input[6]==marker)or
        (game_input[7]==game_input[8]==game_input[9]==marker) or
         (game_input[7]==game_input[5]==game_input[3]==marker) or
          (game_input[1]==game_input[5]==game_input[9]==marker) or
           (game_input[1]==game_input[4]==game_input[7]==marker) or
             (game_input[2]==game_input[5]==game_input[8]==marker) or
            (game_input[3]==game_input[6]==game_input[9]==marker))
#print(win(game_input,'X'))



def choose_player():

    player=random.randint(1,2)
    if player==1:
        return 'player1'
    else:
        return 'player2'
#empty space check
def space(game_input,position):
    return game_input[position] ==' '

#full board check
def full_board_check(game_input):
    for i in range(1,10):
        if space(game_input,i):
            return False
    return True

#player choice of marker place
def player_choice(game_input):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
        position=int(input('please choose your position (1-9)on your numpad:'))
    return position

#would you like to play again
def play_again():
    choice=input('would you like to play again [Y/N]:')
    return choice=="Y"


while True:
    the_board =[' ']*10
    player_1,player_2=player_input()
    print(player_1+'is player 1 sign')
    print(player_2 + 'is player 2 sign')

    turn=choose_player()
    print(turn+'will play first')

    play_game=input('are you ready to play [Y/N]:')
    if play_game=='Y':
        game_on =True
    else:
        game_on =False

    while game_on:
        if turn=='player_1':
            board(the_board)
            position=player_choice(the_board)
            put_marker(the_board,player_1,position)

            if win(the_board,player_1):
                board(the_board)
                print('player 1 has won yeyeyeye')
                game_on= False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('game tie')
                    game_on= False
                else:
                        turn='player_2'
        else:
            board(the_board)
            position=player_choice(the_board)
            put_marker(the_board,player_2,position)

            if win(the_board,player_2):
                    board(the_board)
                    print('player2 has won yeyeyeye')
                    game_on= False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('game tie')
                    game_on= False
                else:
                    turn='player_1'


    if not play_again():
        break
