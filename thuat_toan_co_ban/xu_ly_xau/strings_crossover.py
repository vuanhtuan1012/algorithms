# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-16 23:01:07
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-16 23:04:12

"""
Định nghĩa phép toán crossover của hai xâu có độ dài bằng nhau A và B như sau:
- Kết quả của phép toán này là một xâu result có độ dài bằng với hai xâu đầu vào.
- result[i] bằng A[i] hoặc B[i].

Cho một danh sách các xâu có độ dài bằng nhau inputArray và một xâu result,
hãy đếm xem có bao nhiêu cặp xâu trong mảng đã cho mà
kết quả của phép toán crossover cho ra kết quả là result.

Ví dụ:
Với inputArray = ["abc", "aaa", "aba", "bab"] và result = "bbb",
kết quả stringsCrossover(inputArray, result) = 2.
Có 2 cặp xâu kí tự thỏa mãn yêu cầu đề bài là:
- abc vs bab
- aba vs bab
"""
