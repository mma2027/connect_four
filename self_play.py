import random

from helper import(
    create_board, check_win, is_draw, get_valid_moves, drop_piece, print_board
)

from engines import(
    engineR
)

def self_play(engine1, engine2, record_states=True):

    board = create_board()
    current_player = 1
    ai_states = []

    while True:
        # Terminal check first to avoid calling moves on a full/finished board
        if check_win(board, 1):
            print_board(board)
            return 1, ai_states
        if check_win(board, 2):
            print_board(board)
            return 2, ai_states
        if is_draw(board):
            print_board(board)
            return None, ai_states

        # Record state whenever it's our chosen AI player's turn
        if record_states:
            ai_states.append(([row[:] for row in board], current_player))  # deep copy

        moves = get_valid_moves(board)
        if not moves:
            # Safety net: treat as draw
            return None, ai_states
        if current_player == 1:
            col = engine1(board, current_player)
        else:
            col = engine2(board, current_player)
        drop_piece(board, col, current_player)

        # Switch player
        current_player = 2 if current_player == 1 else 1

def simulate(engine1, engine2, games=1):
    win1 = 0
    win2 = 0
    draw = 0
    ai_states = []
    for _ in range(games):
        result, states = self_play(engine1, engine2)
        # print(len(states))
        ai_states.append(states)
        if result == 1:
            win1 += 1
        elif result == 2:
            win2 += 1
        else:
            draw += 1
    print(win1, win2, draw)
    # print(ai_states)
    return ai_states
self_play(engineR, engineR)

simulate(engineR, engineR, 1)