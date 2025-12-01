import os
import sys

ROWS = 6
COLS = 7

# ANSI color codes
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"

RED    = "\033[31m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"


USE_COLORS = True  # set to False if your terminal is weird


def create_board():
    """Return an empty ROWS x COLS board filled with 0s."""
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def check_win(board, player):
    """Return True if `player` has 4 in a row somewhere."""
    # Horizontal check
    for r in range(ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == player and
                board[r][c+1] == player and
                board[r][c+2] == player and
                board[r][c+3] == player):
                return True

    # Vertical check
    for c in range(COLS):
        for r in range(ROWS - 3):
            if (board[r][c] == player and
                board[r+1][c] == player and
                board[r+2][c] == player and
                board[r+3][c] == player):
                return True

    # Diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (board[r][c] == player and
                board[r+1][c+1] == player and
                board[r+2][c+2] == player and
                board[r+3][c+3] == player):
                return True

    # Diagonal (up-right)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == player and
                board[r-1][c+1] == player and
                board[r-2][c+2] == player and
                board[r-3][c+3] == player):
                return True

    return False

def is_draw(board):
    """Return True if the board is full and no one has won."""
    return len(get_valid_moves(board)) == 0

def get_valid_moves(board):
    """Return a list of column indices (0-based) that are not full."""
    return [c for c in range(COLS) if board[0][c] == 0]

def drop_piece(board, col, player):
    """
    Drop a piece for `player` (1 or 2) into column `col` (0-based).
    Returns True if successful, False if column is full.
    """
    for r in range(ROWS-1, -1, -1):  # start from bottom row
        if board[r][col] == 0:
            board[r][col] = player
            return True
    return False  # column full

def print_board(board, current_player=None):
    clear_screen()

    # Title
    title = " CONNECT FOUR "
    print()
    print(color("╔" + "═" * len(title) + "╗", CYAN, BOLD))
    print(color("║", CYAN, BOLD) + color(title, BOLD, WHITE) + color("║", CYAN, BOLD))
    print(color("╚" + "═" * len(title) + "╝", CYAN, BOLD))
    print()

    # Turn indicator
    if current_player is not None:
        symbol = "X" if current_player == 1 else "O"
        piece = render_cell(current_player)
        print(f" Turn: Player {current_player} ({symbol}) {piece}\n")

    # Column numbers
    print("  " + "  " + " ".join(str(c + 1) for c in range(COLS)))

    inner_width = 2 * COLS + 1
    print("  " + color("┌" + ("─" * inner_width) + "┐", CYAN))

    # Rows
    for r in range(ROWS):
        row_pieces = [render_cell(board[r][c]) for c in range(COLS)]
        line = (
            "  "
            + color("│", CYAN)
            + " "
            + " ".join(row_pieces)
            + " "
            + color("│", CYAN)
        )
        print(line)

    # Bottom border
    print("  " + color("└" + ("─" * inner_width) + "┘", CYAN))
    print()

def render_cell(value):
    """Return a pretty colored string for a single cell (fixed-width)."""
    if value == 0:
        return color(".", DIM, WHITE)        # empty
    elif value == 1:
        return color("X", BOLD, RED)         # Player 1
    else:
        return color("O", BOLD, YELLOW)      # Player 2

def clear_screen():
    # Try to clear the terminal in a cross-platform way
    if os.name == "nt":
        os.system("cls")
    else:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

    

def color(text, *codes):
    if not USE_COLORS:
        return text
    return "".join(codes) + text + RESET

def board_to_vector(board, player):
    vector = []
    for row in board:
        for col in row:
            if col == player:
                vector.append(1)
            else:
                vector.append(0)
    for row in board:
        for col in row:
            if col != player and col != 0:
                vector.append(1)
            else:
                vector.append(0)
    return vector