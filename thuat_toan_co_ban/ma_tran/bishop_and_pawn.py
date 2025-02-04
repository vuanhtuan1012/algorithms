# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-04 15:51:04
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-04 17:14:31

"""
Bàn cờ vua là một bảng có 8*8 ô vuông.
Mỗi ô trên bàn cờ được kí hiệu bằng 2 kí tự - 1 kí tự chữ cái và 1 kí tự số.

- Các cột hàng dọc được gán nhãn từ trái sang phải bằng các kí tự chữ cái từ 'a' tới 'h'.
- Các hàng ngang được đánh số từ 1 tới 8 từ phía dưới lên trên.
- Vị trí mỗi một ô trên bàn cờ được thể hiện bằng xâu có 2 kí tự:
  - kí tự đầu tiên thể hiện cột,
  - kí tự thứ hai thể hiện hàng.
  Ví dụ như a8, b3, c2, ...

Cho tọa độ tượng trắng bishop và tốt đen pawn trên bàn cờ tiêu chuẩn.
Kiểm tra xem tượng trắng có thể ăn tốt đen trong một nước đi hay không?

Ví dụ:
- bishopAndPawn("a1", "c3") = True
- bishopAndPawn("h1", "h3") = False
"""

from typing import List, Tuple


def coordinate_to_square(coordinate: Tuple[int, int]) -> str:
    """
    Returns the square of the given coordinate
    """
    col, row = coordinate
    return f"{chr(col)}{row}"


def get_capturable_squares(bishop_square: str) -> List[str]:
    """
    Returns list of squares which are capturable by the given bishop square
    """
    capturable_squares = []
    bishop_col, bishop_row = ord(bishop_square[0].upper()), int(bishop_square[1])

    # first quadrant
    cur_col, cur_row = bishop_col, bishop_row
    while cur_col < ord("H") and cur_row < 8:
        cur_col += 1
        cur_row += 1
        capturable_squares.append(coordinate_to_square((cur_col, cur_row)))

    # second quadrant
    cur_col, cur_row = bishop_col, bishop_row
    while cur_col > ord("A") and cur_row < 8:
        cur_col -= 1
        cur_row += 1
        capturable_squares.append(coordinate_to_square((cur_col, cur_row)))

    # third quadrant
    cur_col, cur_row = bishop_col, bishop_row
    while cur_col > ord("A") and cur_row > 1:
        cur_col -= 1
        cur_row -= 1
        capturable_squares.append(coordinate_to_square((cur_col, cur_row)))

    # forth quadrant
    cur_col, cur_row = bishop_col, bishop_row
    while cur_col < ord("H") and cur_row > 1:
        cur_col += 1
        cur_row -= 1
        capturable_squares.append(coordinate_to_square((cur_col, cur_row)))

    return capturable_squares


def is_capturable(bishop_square: str, pawn_square: str) -> bool:
    """
    Returns True if the given bishop can capture the given paw, otherwise False
    """
    return pawn_square.upper() in get_capturable_squares(bishop_square)
