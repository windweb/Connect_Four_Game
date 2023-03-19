import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    # if this condition is true we will let the use drop piece here.
    # if not true that means the col is not vacant
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

'''
def print_board(board):
    print(np.flip(board, 0))
'''

def print_board(board):
    for r in range(ROW_COUNT-1, -1, -1):
        row = "|"
        for c in range(COLUMN_COUNT):
            if board[r][c] == 0:
                row += "_|"
            elif board[r][c] == 1:
                row += "X|"
            else:
                row += "O|"
        print(row)


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1, Make your Selection(0-6):"))
        # Player 1 will drop a piece on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            if winning_move(board, 1):
                print("Congratulations Player 1, You won!")
                game_over = True
            elif np.count_nonzero(board) == ROW_COUNT * COLUMN_COUNT:
                print("Game over. It's a stalemate.")
                game_over = True

    # Ask for player 2 input
    else:
        col = int(input("Player 2, Make your Selection(0-6):"))
        # Player 2 will drop a piece on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if winning_move(board, 2):
                print("Congratulations Player 2, You won!")
                game_over = True
            elif np.count_nonzero(board) == ROW_COUNT * COLUMN_COUNT:
                print("Game over. It's a stalemate.")
                game_over = True

    print_board(board)

    turn += 1
    turn = turn % 2




'''
Connect Four is a 2-player game. Players
alternate taking turns. Each side of the
Connect Four board has its own color of
checkers. There is one color for each player.
The goal of Connect Four is to get 4 of your
color checkers in a row—horizontally,
vertically, or diagonally—before your
opponent does!
When it is your turn, drop 1 of your checkers
into the open slot at the top of the Connect
Four board. This allows you to either build
your row or stop your opponent from
getting 4 in a row. After you drop your
checker, it’s your opponent’s turn.
The game is over when one player gets 4
checkers in a row, or when all slots are filled,
meaning the game ends in a stalemate.
To play again, pull the slides out of the
bottom of the board, releasing the checkers
onto the ground. There is one slide on each
end of the board.
Happy Connect Four-ing!
'''

'''
Connect Four - это игра для двух игроков. Игроки чередуются по очереди. 
Каждая сторона доски Connect Four имеет свой цвет шашки. 
Для каждого игрока существует один цвет.
Цель игры "Соедини четыре" - собрать 4 шашки своего цвета шашек в ряд 
- по горизонтали, по вертикали или диагонали - до того, как это сделает ваш до того, 
как это сделает ваш противник!
Когда наступит ваша очередь, опустите 1 из ваших шашек в открытый слот в верхней части доски Connect 4. 
Это позволит вам либо построить свой ряд или помешать противнику получить 4 шашки в ряд. 
После того, как вы бросите свою шашку, наступает очередь вашего противника.
Игра заканчивается, когда один из игроков получает 4 шашек подряд или когда все слоты заполнены, 
то есть игра заканчивается в тупике.
Чтобы сыграть снова, вытащите полозья из из нижней части доски, освободив шашки на землю. 
На каждом конце доски.
Счастливой игры!
'''
