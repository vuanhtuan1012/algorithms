# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-04 15:51:04
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-04 23:39:18

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

from typing import Tuple


def square_to_coordinate(square: str) -> Tuple[int, int]:
    """
    Returns the coordinate of the given square
    """
    return ord(square[0].upper()), int(square[1])


def is_capturable(bishop_square: str, pawn_square: str) -> bool:
    """
    Returns True if the given bishop can capture the given paw, otherwise False
    """
    bishop_coordinate = square_to_coordinate(bishop_square)
    pawn_coordinate = square_to_coordinate(pawn_square)
    return (
        abs(bishop_coordinate[0] + pawn_coordinate[0])
        == abs(bishop_coordinate[1] + pawn_coordinate[1])
        and bishop_coordinate[0] != pawn_coordinate[0]
    )
