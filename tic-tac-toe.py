print("Hello! Welcome to the Tic-Tac-Toe game!")

def create_grid():
    """Creates a list of nine interges
    Return: A list of interges
    """
    board = [1,2,3,4,5,6,7,8,9]
    return board

def draw_grid(board):
    """Prints out a grid of 3x3 squares.
    Returns: Nothing
    """
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

draw_grid(create_grid())