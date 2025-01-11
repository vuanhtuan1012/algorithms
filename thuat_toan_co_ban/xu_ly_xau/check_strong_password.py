# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-11 23:35:02
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-11 23:36:23

"""
Một trang web định nghĩa 1 mật khẩu được gọi là mạnh (strong) nếu đảm bảo các yếu tố sau:

Có độ dài tối thiểu là 6
Chứa ít nhất 1 chữ số (1234567890)
Chứa ít nhất kí tự chữ cái in thường (abc...z)
Chứa ít nhất 1 kí tự chữ cái in hoa (ABC...Z)
Chứa ít nhất 1 kí tự đặc biệt: !@#$%^&*()-+

Ví dụ:
- checkStrongPassword("abc") = false
- checkStrongPassword("Aa1!") = false
- checkStrongPassword("Aabc1!") = true
"""