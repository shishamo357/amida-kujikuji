# amida_solver.py

def follow_amida_path(grid, start_pos):
    """
    あみだくじをたどって、最終的に到達する位置を返す。

    :param grid: あみだくじの2次元リスト（横×縦）
    :param start_pos: 開始位置（整数）
    :return: ゴール位置（整数）
    """
    x = start_pos
    for row in grid:
        # 左に橋があれば左へ
        if x > 0 and row[x - 1]:
            x -= 1
        # 右に橋があれば右へ
        elif x < len(row) - 1 and row[x]:
            x += 1
        # それ以外は下へ xはそのまま
    return x

