# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-19 17:35:23
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-19 17:37:25

"""
Cho một xâu kí tự, viết hàm mã hóa xâu đó theo các luật sau:
- Đầu tiên, cắt xâu ban đầu thành các xâu con mà mỗi xâu con chỉ
  chứa các kí tự giống nhau và xâu con tạo ra có độ dài là lớn nhất
  - Ví dụ: xâu "aabbbc" được tách thành ["aa", "bbb", "c"]
- Tiếp theo, với mỗi xâu con có chiều dài lớn hơn 1, hãy thay thế xâu đó
  bằng việc viết liền độ dài của xâu với kí tự lặp lại.
  - Ví dụ: xâu con "bbb" được thay thế bằng "3b"
- Cuối cùng, viết liên tiếp các xâu con vừa được mã hóa theo thứ tự ban
  đầu để tạo ra xâu kết quả.

- Ví dụ: lineEncoding("aabbbc") = "2a3bc"
"""
