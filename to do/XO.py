#Ćwiczenia Pythona "Pyton dla każdego" M. Dawson


#XO, computer vs user

#global values
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#display instruction
def display_instr():
    print(
        """
        WELCOME TO XO
        You will play this game against me - your computer. 

        Choose number between 0-8. It represents a position on board as follows:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

        Get ready! You will need luck to win ;)
        """
        )

# asks quetion with possible answer "yes" or "no"
def ask_yes_no(question):
    response = None
    while response not in ("yes", "no"):
        response = input(question).lower()
    return response

# sets how is doing the first move
def pieces():
    go_first = ask_yes_no("Do you want to make a first move? (yes/no): ")
    if go_first == "yes":
        print("Go ahead...")
        user = X
        computer = O
    else:
        print("Sit and watch closely!")
        computer = X
        user = O
return computer, user

# create a board
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
return board

#display board
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "_________")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "_________")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

# possible moves
def poss_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            move.append(square)
    return moves

# and the winner is
def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

# user move
def user_move(board, user):
    poss = poss_moves(board)
    move = None
    while move not in poss:
        move = ask_number("You move? Number (0-8): ", NUM_SQUARES)
        if move not in legla:
            print("It is not empty!. Choose else.")
    print("Ok")
    return move

#computer move
def computer_move(board, computer, user):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I choose number", end=" ")
    for move in poss_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in poss_moves(board):
        board[move] = user
        if winner(board) == user:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in poss_moves(board):
            print(move)
            retunr(move)

# your turn
def next_turn(turn):
    if turn == X:
        return 0
    else:
        return X

#congratulations
def congrat(winner, computer, user):
    if winner != TIE:
        print(winner, "has won")
    else:
        print("Remis"

#main
def main():
    display_instr()
    computer, user = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == user:
            move = user_move(board, user)
            board[move] = user
        else:
            move = computer_move(board, computer, user)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    winner = winner(board)
    congrat(winner, computer, user)


#start
main()
input("\n\nPress "Enter" to quit")
            
                  
    
















    
        


        
    
        
    

