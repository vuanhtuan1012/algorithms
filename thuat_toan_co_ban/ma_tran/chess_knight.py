# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-05 16:08:03
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-05 16:13:44

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