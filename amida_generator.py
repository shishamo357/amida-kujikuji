import random

def generate_amida(height=10, width=5):
    # 盤面を作る：Falseなら横線なし、Trueなら横線あり
    board = [[False for _ in range(width - 1)] for _ in range(height)]

    for y in range(height):
        for x in range(width - 1):
            # 横線を置くかどうかはランダム、ただし連続は避ける
            if x > 0 and board[y][x - 1]:
                continue  # 直前に横線があればスキップ
            board[y][x] = random.choice([True, False])

    return board

def print_amida(board):
    width = len(board[0]) + 1

    for row in board:
        line = "|"
        for x in range(width - 1):
            if row[x]:
                line += "―|"
            else:
                line += " |"
        print(line)

if __name__ == "__main__":
    board = generate_amida(height=10, width=5)
    print_amida(board)

    """
# 使用例（テスト用）
from amida_solver import follow_amida_path

start = 2
goal = follow_amida_path(grid, start)
print(f"スタート位置 {start} → ゴール位置 {goal}")
"""
# ↑テスト用のあみだくじデータ　使うときはコメントアウト外して～
