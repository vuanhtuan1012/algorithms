# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-10 00:00:06
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-10 00:07:17

"""
Chuyển tin

Cần chuyển hết n gói tin trên một mạng gồm m kênh truyền.
Biết chi phí chuyển i gói tin trên kênh j là C(i, j) (1 <= C(i, j) <= 10000).

Yêu cầu: cho biết một phương án chuyển gói tin với chi phí thấp nhất.
Dữ liệu:
- Dòng 1: hai số n và m (1 <= n, m <= 100)
- Dòng thứ i trong n dòng tiếp theo: dãy m số nguyên dương C1, C2..., Cm
  trong đó Cj là chi phí chuyển i gói tin trên kênh j.

Kết quả:
- dòng đầu tiên: tổng chi phí thấp nhất theo phương án tìm được.
- dòng thứ j trong m dòng tiếp theo: số lượng gói tin chuyển trên kênh j.

Ví dụ:
- File input: messages.inp
5 4
31 10  1  1
 1 31 12 13
 4 10 31  1
 6  1 20 19
10  5 10 10
- File output: messages.out
2
0
4
1
0
"""