# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-19 17:35:23
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-24 12:18:19

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


def encode_line(line: str) -> str:
    """
    Returns encoded line of the given line
    """
    current_letter = ""
    no_occurrence = 0
    encoded_line = ""
    for letter in line:
        if not current_letter:
            current_letter = letter
        if letter == current_letter:
            no_occurrence += 1
        else:
            encoded_line += (
                current_letter
                if no_occurrence == 1
                else f"{no_occurrence}{current_letter}"
            )
            current_letter = letter
            no_occurrence = 1
    encoded_line += (
        current_letter if no_occurrence == 1 else f"{no_occurrence}{current_letter}"
    )
    return encoded_line


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("aabbbc", "2a3bc"),
        ("abbcabb", "a2bca2b"),
        ("abcd", "abcd"),
        ("zzz", "3z"),
        ("wwwwwwwawwwwwww", "7wa7w"),
    ]
    for i, (line, ground_truth) in enumerate(test_cases):
        result = encode_line(line)
        print(f"Test case {i+1}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
