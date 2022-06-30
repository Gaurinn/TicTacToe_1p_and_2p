#tic tac toe game for 1 vs computer or 2 players

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#global variables player names
player1Name = " "
player2Name = " "

#global variable for one player or two player game
onePlayer = True

#display the game instructions
def display_instructions():
    """ Display the game instructions"""
    print(
        """
        Welcome to Tic Tac Toe
        Make your move by entering a number corresponding to
        the board position 

            0 | 1 | 2
            _________
            3 | 4 | 5
            _________
            6 | 7 | 8
        
        Get ready to play
        """
    )

#ask one player game vs computer or 2 player game
def one_v_cpu_or_2p():
    global onePlayer
    response = None
    while response not in (1, 2):
        response = int(input("Would you like to play against the computer or a 2 player game? (select 1 or 2) "))
    if response == 1:
        onePlayer = True
    elif response == 2:
        onePlayer = False

#ask for player names
def ask_player_names():
    global player1Name
    global player2Name
    player1Name = input("What is the name for player 1? ")
    player2Name = input("What is the name for player 2? ")
    while player1Name == player2Name:
        player2Name = input("Choose a different name for player 2? ")
    return player1Name, player2Name

#ask who goes first
def ask_who_goes_first(question, player1, player2):
    """Ask who goes first"""
    if onePlayer:
        response = None
        while response not in ("y", "n"):       
            response = input(question).lower()
        return response
    else:              
        response = None
        while response not in (player1, player2):       
            response = input(question)
        return response

#ask for a number, or a move to play
def ask_number(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

#determine who is X and who is O, X goes first
def pieces():
    """Get player names and who is X and who is O"""
    if onePlayer:
        go_first = ask_who_goes_first("Do you want to go first? Yes or No: y/n ", X, O)
        if go_first == "y":
            print("You are X and take the first move")
            computer = O
            player = X
        else:
            print("You are O and the computer takes the first move")
            computer = X
            player = O
        return computer, player
    else:    
        player1, player2 = ask_player_names()
        go_first = ask_who_goes_first(("Who goes first, " + player1Name + " or " + player2Name + "? "), player1, player2)
        if go_first == player1Name:
            print(player1Name, "You are X and take the first move")
            player1 = X
            player2 = O
        else:
            print(player2Name, "You are X and take the first move")
            player1 = O
            player2 = X
        return player1, player2, player1Name, player2Name

#create a new empty board
def new_board():
    """Create a new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#display the game board
def display_board(board):
    """Display the game board on screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "_________")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "_________")
    print("\n\t", board[6], "|", board[7], "|", board[8])
    
#make sure a move is legal
def legal_moves(board):
    """Create a list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

#winning conditions
def winner(board):
    """Winning conditions"""
    WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))

    #see if X or O is in all three spaces in a row of ways_to_win and return a winner
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    #see if there are any moves left, if not then tie
    if EMPTY not in board:
        return TIE

    #if no winner yet and there are moves to be made then continue with the game
    return None

#player move
def player_move(board, player):
    """Get the player move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        if len(legal) > 7:
            move = ask_number(("What is your first move? " + player + "( 0 - 8:) "), 0, NUM_SQUARES)
        else:
            move = ask_number(("What is your next move? " + player + "( 0 - 8:) "), 0, NUM_SQUARES)
        if move not in legal:
            print("That is an illegal move, try again")
        print("You made your move")
    return move

#computer move
def computer_move(board, computer, player):
    """Make computer move"""
    #make a copy of the board
    board = board[:]

    #the best positions to have on the board, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Computer moves to", end=" ")

    #check if computer can win, then take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #if computer move did not return a winning move, then try something else
        board[move] = EMPTY

    #check if player can win in next move, then block that move
    for move in legal_moves(board):
        board[move] = player
        if winner(board) == player:
            print(move)
            return move
        #if player can not win in next move, then try something else
        board[move] = EMPTY

    #since no one can win in the next move, pick the best move
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

#next to make a move
def next_turn(turn):
    """Switch turns"""
    if turn == "X":
        return O
    else:
        return X

#Game over
def who_is_winner(the_winner, computer, player):
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It´s a tie\n")

    if the_winner == computer:
        print("The computer beat you\n")

    elif the_winner == player:
        print("You beat the computer\n")

    elif the_winner == TIE:
        print("No one wins")

def who_is_winner(the_winner, player1, player2):
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It´s a tie\n")

    if onePlayer:
        if the_winner == player1:
            print("The computer beat you\n")

        elif the_winner == player2:
            print("You beat the computer\n")
    else:

        if the_winner == player1:
            print(player1Name, "is the winner!\n")

        elif the_winner == player2:
            print(player2Name, "is the winner!\n")

    if the_winner == TIE:
        print("No one wins")

def main():
    display_instructions()
    board = new_board()
    turn = X
    one_v_cpu_or_2p()
    if onePlayer:
        computer, player = pieces()
        display_board(board)
        while not winner(board):
            if turn == player:
                move = player_move(board, player)
                board[move] = player
            else:
                move = computer_move(board, computer, player)
                board[move] = computer
            display_board(board)
            turn = next_turn(turn)
    else:
        player1, player2, player1Name, player2Name = pieces()
        display_board(board)
        while not winner(board):
            if turn == player1:
                move = player_move(board, player1Name)
                board[move] = player1
            else:
                move = player_move(board, player2Name)
                board[move] = player2
            display_board(board)
            turn = next_turn(turn)
        
    the_winner = winner(board)
    if onePlayer:
        who_is_winner(the_winner, computer, player)
    else:
        who_is_winner(the_winner, player1, player2)
main()
input("Press the enter key to quit")

    