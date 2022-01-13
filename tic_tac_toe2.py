"""
Python Tic-Tac-Toe
By Diane Silla
"""
def main():

    player = whose_turn("")
    board = create_board()
    win = check_win(board)
    draw = check_draw(board)

    create_board()

    print(f"\n {board[0]} | {board[1]} | {board[2]} \n-----------\n {board[3]} | {board[4]} | {board[5]} \n-----------\n {board[6]} | {board[7]} | {board[8]} \n")


    while not (win or draw):

        user_input(board, player)

        #print(board)

        player = whose_turn(player)

        win = check_win(board)

        draw = check_draw(board)



def create_board():
    """
    This function creates the list of numbers included in the tic-tac-toe board. Reminder that indexes = number - 1
    Parameters: none
    Return: board"""

    board=  [1, 2, 3, 4, 5, 6, 7, 8, 9]

    return board


def user_input(board, player):
    """
    This function asks for the player's input and replaces that number on the board (list and display) with x or o. The updated board is printed.
    Parameters = the board (which is the list) and the player (x or o)
    Return = the updated board (list)
    """

    user_input = int(input(f"Player {player}, Make your move (1-9): "))
    player_slot = user_input - 1

    board[player_slot] = player
    
    print(f"\n {board[0]} | {board[1]} | {board[2]} \n-----------\n {board[3]} | {board[4]} | {board[5]} \n-----------\n {board[6]} | {board[7]} | {board[8]} \n")

    return board

def whose_turn(player):
    """
    This function toggles players back and forth.
    Parameters = the current player
    Returns = the next player
    """

    if player == "" or player == "o":
        return "x"
    elif player == "x":
        return "o"

def check_win(board):
    """
    This function interates through all possible winning combinations. If a player has won, they will receive congratulations and the game will end.
    Parameters = the udpated board (list)
    Return = True (for a win) or False 
    """
    if board[0] == board[1] == board[2] or \
        board[3] == board[4] == board[5] or \
        board[6] == board[7] == board[8] or \
        board[0] == board[3] == board[6] or \
        board[1] == board[4] == board[7] or \
        board[2] == board[5] == board[8] or \
        board[0] == board[4] == board[8] or \
        board[2] == board[4] == board[6]:
        print("Congratulations, you won!")
        return True
    else: 
        return False

def check_draw(board):
    """
    This function checks for a draw by counting the number of x and o on the board (list). In the event of a draw, it is announced and the game will end.
    Parameters = the updated board (list)
    Return = True (for a draw) or False
    """

    x = board.count("x")
    o = board.count("o")

    num_turns = x + o
    #print(num_turns)

    if num_turns == 9:
        print("It is a draw!")
        return True
    else:
        return False

if __name__ == "__main__":
    main()