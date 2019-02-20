import random
#function that can print out a board
def display_board(board):
    print('\n' * 100)
    print (board[1]+'|'+board[2]+'|'+board[3])
    print ('-----')
    print (board[4] + '|' + board[5] + '|' + board[6])
    print ('-----')
    print (board[7] + '|' + board[8] + '|' + board[9])

#To decide the marker for each player
def player_input():
    player1 = raw_input("Player1: Please pick a marker 'X' or 'O' ").upper()
    if(player1=='X'):
        return ('X','O')
    else:
        return ('O', 'X')

#to mark on the board
def place_marker(board, marker, position):
    board[position]=marker

#If any one wins
def win_check(board, mark):
    return(board[1]==board[2]==board[3]==mark or
           board[4] == board[5] == board[6]==mark or
           board[7] == board[8] == board[9]==mark or
           board[1] == board[4] == board[7]==mark or
           board[2] == board[5] == board[8]==mark or
           board[3] == board[6] == board[9]==mark or
           board[1] == board[5] == board[9]==mark or
           board[3] == board[5] == board[7]==mark)

#to get the first player
def choose_first():
     player = random.randint(0, 1)
     if player == 0:
         return ('Player 1')
     else:
         return ('Player 2')

#to check if the entered position is empty
def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False

#to check if the board is full
def full_board_check(board):
    for i in range(1, 10):
        if not space_check(board, i):
            return False
        return True

#To take in the position input
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position= int(raw_input("Enter position: "))
    return (position)


#for replay
def replay():
    choice=raw_input("Replay? Y or N ").upper()
    if choice=="Y":
        return True

while True:
    # Set the board
    test_board = [' '] * 10
    display_board(test_board)
    #choose who is the first player
    turn = choose_first()
    # Choose the markers
    Player1,Player2=player_input()
    # Ask the player if ready or not
    Ready=raw_input("Ready? Y or N ").upper()
    game_on=True
    if Ready=="Y":
    # Play the game
        while game_on:
        # Player 1 Turn
            if turn == 'Player 1':
        #show the board
                display_board(test_board)

        # Choose the position
                position=player_choice(test_board)
        # place the marker on the position
                place_marker(test_board, Player1, position)
        # check if won
                if win_check(test_board,Player1):
                    print("Player 1 wins")
                    game_on=False

        # check if Tie or not
                if full_board_check(test_board):
                    print("Its a tie")
                    game_on=False
        # no tie no win? next player turn
                turn='Player 2'
        # Player2's turn.
            else:
            # show the board
                display_board(test_board)

            # Choose the position
                position = player_choice(test_board)
            # Check if the entered position is empty
                place_marker(test_board, Player2, position)
            # check if won
                if win_check(test_board, Player2):
                    print("Player2 wins")
                    game_on = False

                # check if Tie or not
                if full_board_check(test_board):
                    print("Its a tie")
                    game_on = False
                turn='Player 1'

        if not replay():
            break


