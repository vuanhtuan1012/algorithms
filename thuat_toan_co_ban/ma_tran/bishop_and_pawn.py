# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-04 15:51:04
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-04 15:54:00

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
