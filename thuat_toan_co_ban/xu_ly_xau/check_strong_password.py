# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-11 23:35:02
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-12 00:12:50

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


def is_strong_password(password: str) -> bool:
    """
    Returns True if the given password is trong, otherwise False
    """
    special_characters = set("!@#$%^&*()-+")
    return (
        len(password) >= 6
        and any(char.isdigit() for char in password)
        and any(char.islower() for char in password)
        and any(char.isupper() for char in password)
        and any(char in special_characters for char in password)
    )


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("abc1", False),
        ("Ab1!", False),
        ("Aa123A!", True),
        ("AAAAAAAAAAAAAA", False),
        ("ABC1&!aaaa", True),
        ("AAAAaaa", False),
    ]
    for password, ground_truth in test_cases:
        result = is_strong_password(password)
        print(f"is_strong_password({password}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
