# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-15 02:18:01
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-16 15:28:47

"""
Bài 2. Mạch DNA

Cho mạch mã gốc DNA bốn loại nucleotide A, T, G, C.
Để tiết kiệm bộ nhớ, mạch mã gốc đã được nén lại thành một chuỗi S
gồm các cặp là số lần xuất hiện liên tiếp nucleotide và loại nucleotide tương ứng.
Ví dụ: mạch mã gốc AACAATGGGGA nén thành 3A1C2A1T4G1A
Các nucleotide ở hai mạch của phân tử DNA liên kết với nhau theo nguyên tắc bổ sung,
trong đó A liên kết với T, G liên kết với C. Do vậy, nếu biết trình tự nucleotide trên
một mạch có thể suy ra trình tự của mạch còn lại.
Ví dụ: một đoạn phân tử DNA ở sinh vật nhân thực có trình tự nucleotide trên mạch mã gốc
là AACAATGGGGA. Trình tự nucleotide trên mạch bổ sung của đoạn DNA này là: TTTGTTACCCCT.

Yêu cầu: Cho một chuỗi kí tự S mô tả mạch mã gốc DNA sau khi đã nén.
Hãy lập trình xác định mạch bổ sung của mạch mã gốc sau khi giải nén.
- File input: machdna.inp
5A2G1A11T1C
- File output: machdna.out
TTTTTCCTAAAAAAAAAAAG
"""
from typing import List, Tuple


def doc_file(filename: str) -> str:
    """
    Returns the compressed DNA strand get from the first line of file
    """
    print(f"Read file {filename}")
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer, start=1):
            if i == 1:
                return line.strip()
    return ""


def phan_tich_ma_nen(ma_nen: str) -> List[Tuple[int, str]]:
    """
    Returns the list of (number, nucleotide) get from the given compressed DNA strand
    """
    cap_ma_nen = []
    no_occurrences = ""
    for nucleotide in ma_nen:
        if nucleotide.isdigit():
            no_occurrences += nucleotide
        else:
            cap_ma_nen.append((int(no_occurrences), nucleotide))
            no_occurrences = ""
    return cap_ma_nen


def tim_mach_bo_sung(cap_ma_nen: List[Tuple[int, str]]) -> str:
    """
    Returns the complementary DNA strand from parsed DNA strand
    """
    nucleotide_pairs = {"A": "T", "G": "C", "C": "G", "T": "A"}
    mach_bs = ""
    for no_occurrences, nucleotide in cap_ma_nen:
        mach_bs += no_occurrences * nucleotide_pairs[nucleotide]
    return mach_bs


def ghi_file(filename: str, mach_bo_sung: str):
    """
    Writes the complementary DNA strand to file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(mach_bo_sung)
    print(f"The result was successfully written to file {filename}")


def main():
    """
    Main function
    """
    ma_nen = doc_file("data/machdna.inp")
    cap_ma_nen = phan_tich_ma_nen(ma_nen)
    mach_bs = tim_mach_bo_sung(cap_ma_nen)
    ghi_file("data/machdna.out", mach_bs)


if __name__ == "__main__":
    main()
