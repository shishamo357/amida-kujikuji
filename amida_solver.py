# amida_solver.py

def follow_amida_path(grid, start_pos):
    """
スタートからあみだくじを一歩ずつ進んで、最後にたどり着いた場所を返す関数。

:param grid: あみだくじの中身（2次元リストで橋の位置を表す）
:param start_pos: スタート地点（左から何番目か）
:return: ゴール地点（左から何番目か）
    """
 

    x = start_pos
    for row in grid:
        # 左に橋があれば左へ
        if x > 0 and row[x - 1]:
            x -= 1
        # 右に橋があれば右へ
        elif x < len(row) - 1 and row[x]:
            x += 1
        # 何もなければそのまま下でええがな
    return x

