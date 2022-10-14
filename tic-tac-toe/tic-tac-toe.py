"""Tic-Tac-Toe: completed after taking a look on the solution
   Author: Sebastiao Joao Matusse
   Contact: email- matussevalete@gmail.com or mat21026@byui.edu // WhatsApp - +25884 8297 863
"""

def main():
    print("Hello! Welcome to the Tic-Tac-Toe game!")
    player = next_player("")
    grid = create_grid()
    while not (has_winner(grid) or is_a_draw(grid)):
        draw_grid(grid)
        change_numbers(grid, player)
        player = next_player(player)
    draw_grid(grid)
    print("Good game. Thnaks for playing!")

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

def change_numbers(numbers, player):
    prompt = int(input(f"{player}'s turn to choose a square (1-9): "))
    numbers[prompt - 1] = player
            
def has_winner(board):
    """Checks if the square have the same value or not.
    Return: """
    return (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6])

def is_a_draw(board):
    """checks to see if it is a drawer or not
    Return: a boolean
    """
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def next_player(current):
    if current == "" or current == "x":
        return "o"
    elif current =="o":
        return "x"

if __name__ == "__main__":
    main()




""" In the code below! I was trying to construct the software before seeing the sample solution"""
# def draw_grid(number_list):
#     print()    
#     for i in number_list:
#         if i == number_list[2] or i == number_list[5]:
#             print(i)
#             print("-+-+-")
#         elif i==9:
#             print(i)
#         else:
#             print(i, end="|", flush="true")
#     print()

    # for i in numbers:
    #     if next(players_1) == "x":
    #         if i == prompt:
    #             numbers[i + 1] = "x"
    #             print(numbers)
    #     elif next(players_1) == "o":
    #         if i == prompt:
    #             numbers[i + 1] = "o" 
            
        # else:
        #     if next(players) == "o":
        #         if i == prompt:
        #             numbers[i] = next(players)

# draw_grid(numbers)
# start_game(draw_grid(numbers), player_1, player_2)
# prompt = int(input(f"{random.choice([player_1, player_2])}'s turn to choose a square (1-9):"))
# change_numbers(numbers, prompt)
# while game_play:
#     start_game()
        