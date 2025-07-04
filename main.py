# あみだくじ（開発中）順
# 1.本数と数
# 1-2 参加人数かスタート本数で（入力してください）を出力
# 2.横線
# 3.表示
# 4.dokoに到達するかを計算
# 5.結果の表示

import random
# 縦棒の本数（参加者数）
num_players = int(input("参加人数を入力してください: "))

# 行数（高さ）
height = 6

# 横線の構造
ladder = [[False] * (num_players - 1) for _ in range(height)]

# 横線をランダムに配置 ←ランダム　本参照
for row in range(height):
    for col in range(num_players - 1):
        if not ladder[row][col]:
            if col == 0 or not ladder[row][col - 1]:
                if random.choice([True, False]):
                    ladder[row][col] = True

# あみだくじの表示
for row in ladder:
    line = "|"
    for i in range(num_players - 1):
        if row[i]:
            line += "―|"
        else:
            line += " |"
    print(line)

# 各どこに到達するかを計算させる
def trace_path(start_col, ladder):
    col = start_col
    for row in ladder:
        if col < len(row) and row[col]:         # 右に線があるとき
            col += 1
        elif col > 0 and row[col - 1]:          # 左に線があるとき
            col -= 1
    return col

# 結果の表示
# ( A →　〇 ) 理想
print("\n結果:")
labels = [chr(ord('A') + i) for i in range(num_players)]  # A, B, C, D...

for i in range(num_players):
    goal = trace_path(i, ladder)
    print(f"{labels[i]} → {goal + 1} 番")
