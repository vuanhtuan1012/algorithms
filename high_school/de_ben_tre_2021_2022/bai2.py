# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-07 21:22:52
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-07 22:33:28
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

from typing import List, Tuple


def doc_file(filename: str) -> Tuple[int, List[int]]:
    """
    Returns tuple of subsequence total and the list of elements
    """
    print(f"Read file {filename}")
    with open(filename, encoding="utf-8") as file_pointer:
        data = file_pointer.readlines()
    _, tong_doan = map(int, data[0].strip().split())
    day_so = list(map(int, data[1].strip().split()))
    return tong_doan, day_so


def tim_doan(day_so: List[int], tong_doan: int) -> List[Tuple[int, List[int]]]:
    """
    Returns the index (1-index) of starting element along with the list of subsequences
    whose sum of subsequence elements equals the given total
    """
    cac_doan_con = []
    for i, element in enumerate(day_so):
        if element > tong_doan:
            continue
        j = i + 1
        while j < len(day_so) and sum(day_so[i:j]) < tong_doan:
            j += 1
        if sum(day_so[i:j]) == tong_doan:
            cac_doan_con.append((i + 1, day_so[i:j]))
    return cac_doan_con


def tim_doan_ngan_nhat(
    cac_doan_con: List[Tuple[int, List[int]]]
) -> Tuple[int, List[int]]:
    """
    Returns the tuple of the index of starting element along with
    the list of the shortest subsequence
    """
    if not cac_doan_con:
        return 0, 0
    chi_so, doan_ngan_nhat = cac_doan_con[0]
    for idx, doan_con in cac_doan_con:
        if len(doan_con) < len(doan_ngan_nhat):
            chi_so = idx
            doan_ngan_nhat = doan_con
    return chi_so, doan_ngan_nhat


def ghi_file(filename: str, *args: Tuple[int, ...]):
    """
    Writes the result into file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(" ".join(map(str, args)))
    print(f"The result is written to file {filename}")


def main():
    """
    Main function
    """
    tong_doan, day_so = doc_file("data/tdoan.inp")
    cac_doan_con = tim_doan(day_so, tong_doan)
    chi_so, doan_ngan_nhat = tim_doan_ngan_nhat(cac_doan_con)
    if chi_so == 0:
        ghi_file("data/tdoan.out", chi_so)
        return
    ghi_file("data/tdoan.out", chi_so, len(doan_ngan_nhat))


if __name__ == "__main__":
    main()
