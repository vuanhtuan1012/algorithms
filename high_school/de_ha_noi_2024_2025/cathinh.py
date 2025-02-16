# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-15 01:41:51
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-16 11:44:19

"""
Bài 1. Cắt hình

Cho một tờ giấy hình chữ nhật kích thước M(cm) x N(cm) và số tự nhiên K

Yêu cầu: Nếu cắt những hình vuông có kích thước K(cm) x K(cm) từ tờ giấy này
thì diện tích còn lại nhỏ nhất là bao nhiêu cm2?

- File input: cathinh.inp
Gồm ba số tự nhiên M, N, K lần lượt mỗi số trên một dòng (1 <= M, N, K <= 10^9)
8
7
3
- File output: cathinh.out
Một số nguyên duy nhất là kết quả của bài toán
20
"""
from typing import Tuple


def doc_file(filename: str) -> Tuple[int, int, int]:
    """
    Returns tuple of triple numbers read from given file
    """
    print(f"Read file {filename}")
    du_lieu = [0, 0, 0]
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer, start=1):
            if i > 3:
                break
            du_lieu.append(int(line.strip()))
    return tuple(du_lieu)


def tim_dien_tich_con_lai(m: int, n: int, k: int) -> int:
    """
    Returns the smallest remaining area
    """
    chieu_dai = (m // k) * k
    chieu_rong = (n // k) * k
    return m * n - chieu_dai * chieu_rong


def ghi_file(filename: str, dien_tich: int):
    """
    Writes the given area to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(str(dien_tich))
    print(f"The result was successfully written to file {filename}")


def main():
    """
    Main function
    """
    m, n, k = doc_file("data/cathinh.inp")
    dien_tich_con_lai = tim_dien_tich_con_lai(m, n, k)
    ghi_file("data/cathinh.out", dien_tich_con_lai)


if __name__ == "__main__":
    main()
