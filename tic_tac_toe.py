from random import choice
from sty import fg, bg, ef, rs

def print_square(edge_line, side_line, line_with_value):
    print(edge_line)
    print(side_line)
    print(line_with_value)
    print(side_line)


def DisplayBoard(board):
    edge_line =   '+' + '-' * 7 + '+' +  '-' * 7 + '+' +  '-' * 7 + '+'
    side_line =   '|' + ' ' * 7 + '|' +  ' ' * 7 + '|' +  ' ' * 7 + '|'

    for value in board:
        line_with_value =   '|   ' + str(value[0]) + '   ' +\
                            '|   ' + str(value[1]) + '   ' +\
                            '|   ' + str(value[2]) + '   |'

        print_square(edge_line, side_line, line_with_value)
    print(edge_line)


def fill_position_in_board(board, possible_moves, next_move, sign):
    for row in range(3):
        for col in range(3):
            if board[row][col] == next_move:
                possible_moves.remove(board[row][col])
                board[row][col] = sign
                return True
    return False


def computer_move(board, possible_moves):
    next_move = choice(possible_moves)
    fill_position_in_board(board, possible_moves, next_move, fg.red+"X"+fg.rs)
    print("Computer play:")


def EnterMove(board, possible_moves):
    next_move = input("Enter your next move: ")
    while next_move.isdecimal() == False:
        next_move = input("Enter your next move: ")
    next_move = int(next_move)
    while fill_position_in_board(board, possible_moves, next_move,\
                                 fg.li_blue+"O"+fg.rs) == False:
        print(f"Illegal move on {next_move} (already taken), try again")
        next_move = int(input("Enter your next move: "))
    print("Player play:")


def check_board_for_win(board):
    def check_row(board, row):
        return board[row][0] == board[row][1] == board[row][2]

    def check_col(board, col):
        return board[0][col] == board[1][col] == board[2][col]

    def check_diag(board):
        return board[0][0] == board[1][1] == board[2][2] or\
            board[0][2] == board[1][1] == board[2][0]

    for row in range(3):
        for col in range(3):
            if board[row][col] is not int:
                if check_row(board, row) or check_col(board, col)\
                        or check_diag(board):
                    VictoryFor(board[row][col])
                    return True
    return False


def VictoryFor(sign):
    DisplayBoard(board)
    if sign == fg.red+"X"+fg.rs:
        print("Computer won !")
    if sign == fg.li_blue+"O"+fg.rs:
        print("You won !")

def end_in_draw(possible_moves):
    if len(possible_moves) > 0:
        return True
    else:
        print("Draw :(")
        return False

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
possible_moves = [x for x in range(1, 10)]
computer_move(board, possible_moves)
i = 1
while check_board_for_win(board) == False and end_in_draw(possible_moves):
    DisplayBoard(board)
    if i % 2:
        EnterMove(board, possible_moves)
    else:
        computer_move(board, possible_moves)
    i += 1
