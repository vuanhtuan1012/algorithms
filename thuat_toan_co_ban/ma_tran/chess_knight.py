# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-05 16:08:03
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-05 17:42:55

"""
Bàn cờ vua là một bảng có 8*8 ô vuông.
Mỗi ô trên bàn cờ được kí hiệu bằng 2 kí tự - 1 kí tự chữ cái và 1 kí tự số.

- Các cột hàng dọc được gán nhãn từ trái sang phải bằng các kí tự chữ cái từ 'a' tới 'h'.
- Các hàng ngang được đánh số từ 1 tới 8 từ phía dưới lên trên.
- Vị trí mỗi một ô trên bàn cờ được thể hiện bằng xâu có 2 kí tự:
  - kí tự đầu tiên thể hiện cột,
  - kí tự thứ hai thể hiện hàng.
  Ví dụ như a8, b3, c2, ...

Cho biết vị trí của con mã trên bàn cờ vua.
Hãy tìm số vị trí khác nhau mà con mã có thể thực hiện nước nhảy.
"""
from typing import Tuple


def square_to_coordinate(square: str) -> Tuple[int, int]:
    """
    Returns the coordinate of the given square
    """
    return ord(square[0].upper()), int(square[1])


def get_no_positions(knight_square: str) -> int:
    """
    Returns the number of different positions that the given knight can jump to
    """
    # changes in coordinate when the knight move
    changes = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

    no_positions = 0
    current_coordinate = square_to_coordinate(knight_square)
    for col_delta, row_delta in changes:
        col = current_coordinate[0] + col_delta
        row = current_coordinate[1] + row_delta
        if ord("A") <= col <= ord("H") and 1 <= row <= 8:
            no_positions += 1
    return no_positions
