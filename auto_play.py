import random
from main import Othello

def auto_play():
    size = 8  # ゲームボードのサイズを設定
    othello = Othello(size)
    while True:
        if othello.game_over():
            break
        valid_moves = []
        for row in range(size):
            for col in range(size):
                if othello.is_valid_move(row, col):
                    valid_moves.append((row, col))
        if valid_moves:
            row, col = random.choice(valid_moves)
            othello.make_move(row, col)
        else:
            break

    othello.result()

auto_play()
