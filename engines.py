import random

from helper import(
    get_valid_moves
)

def engineR(board, player):
    moves = get_valid_moves(board)
    return random.choice(moves)