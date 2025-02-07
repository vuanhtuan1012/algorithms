# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-07 21:22:52
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-07 21:29:34
"""
Tổng đoạn con

Yêu cầu: Một dãy con gồm các phần tử liên tiếp nhau trong một dãy cho trước được gọi là đoạn.
Cho dãy số gồm N số tự nhiên. Tìm đoạn con ngắn nhất có tổng các phần tử bằng giá trị K cho trước.

Dữ liệu:
- Dòng 1 chứa 2 số nguyên dương N và K (1 <= N <= 2000)
- Dòng 2 chứa N số tự nhiên a1, a2..., an cách nhau một khoảng trắng

Kết quả: Một dòng duy nhất chứa hai số nguyên dương d và L cách nhau khoảng trắng.
Trong đó:
- d: chỉ số của phần tử đầu tiên trong đoạn.
- L: số phần tử trong đoạn (chiều dài đoạn). Nếu vô nghiệm thì in ra số 0.

Ví dụ:
- File input: tdoan.inp
21 17
0 2 3 2 10 1 5 5 6 12 20 30 14 8 0 11 0 6 0 0 5
- File output: tdoan.out
16 3
"""
