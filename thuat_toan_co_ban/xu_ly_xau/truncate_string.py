# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-15 22:19:52
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-15 22:22:00

"""
Cho một xâu kí tự chứa các chữ số từ 0 tới 9.
Người ta áp dụng phép biển đổi xâu dựa trên các nguyên tắc sau:
- nếu chữ số ngoài cùng bên trái chia hết cho 3, xóa nó khỏi xâu kí tự.
- nếu không thỏa mãn điều kiện trên, và nếu chữ số ngoài cùng bên tay phải chia hết cho 3,
  xóa nó khỏi xâu kí tự.
- nếu không thỏa mãn 2 điều kiện trên, và nếu tổng chữ số ngoài cùng bên trái và ngoài
  cùng bên phải chia hết cho 3, xóa cả hai chữ số trên khỏi xâu.
Các phép toán trên được áp dụng vào xâu ban đầu cho tới khi xâu trở thành rỗng,
hoặc ko đáp ứng cả 3 điều kiện trên.

Cho một xâu kí tự, hãy tìm xâu kết quả cuối cùng khi áp dụng liên tục các phép toán trên.

Ví dụ:
- truncateString("312248") = "2"
"""
