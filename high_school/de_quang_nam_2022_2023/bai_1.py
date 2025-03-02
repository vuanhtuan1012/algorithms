# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-03-02 10:10:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-03-02 16:53:59

"""
Bài 1. Thần tượng
"""
from typing import Dict, List


def doc_file(filename: str) -> List[int]:
    """
    Returns danh sach binh chon
    """
    print(f"Read file {filename}")
    ds_binh_chon = []
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i == 0:  # skip the first line
                continue
            ds_binh_chon.append(int(line.strip()))
    return ds_binh_chon


def dem_phieu(ds_binh_chon: List[int]) -> Dict[int, int]:
    """
    Returns so phieu cua cac thi sinh trong danh sach binh chon
    """
    ds_phieu = {}
    for so_bd in ds_binh_chon:
        ds_phieu[so_bd] = ds_phieu.get(so_bd, 0) + 1
    return ds_phieu


def tim_thi_sinh(ds_phieu: Dict[int, int]) -> List[int]:
    """
    Returns danh sach thi sinh duoc binh chon nhieu nhat
    """
    so_phieu_ln = max(ds_phieu.values())
    ds_thi_sinh = []
    for so_bd, so_phieu in ds_phieu.items():
        if so_phieu == so_phieu_ln:
            ds_thi_sinh.append(so_bd)
    return ds_thi_sinh


def sap_xep_thi_sinh(ds_thi_sinh: List[int]):
    """
    Sorts danh sach thi sinh theo thu tu tang dan
    """
    for i in range(len(ds_thi_sinh) - 1):
        for j in range(i + 1, len(ds_thi_sinh)):
            if ds_thi_sinh[j] < ds_thi_sinh[i]:
                ds_thi_sinh[i], ds_thi_sinh[j] = ds_thi_sinh[j], ds_thi_sinh[i]


def ghi_file(filename: str, ds_thi_sinh: List[int]):
    """
    Writes danh sach thi sinh vao file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write("\n".join(map(str, ds_thi_sinh)))
    print(f"Danh sach thi sinh duoc ghi file {filename}")


def main():
    """
    Main function
    """
    ds_binh_chon = doc_file("data/thantuong.inp")
    ds_phieu = dem_phieu(ds_binh_chon)
    ds_thi_sinh = tim_thi_sinh(ds_phieu)
    sap_xep_thi_sinh(ds_thi_sinh)
    ghi_file("data/thantuong.out", ds_thi_sinh)


if __name__ == "__main__":
    main()
