# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-03-11 16:51:14
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-03-11 21:49:51
"""
Bài 2. Hoa giấy
"""

def doc_file(filename: str) -> str:
    """
    Returns danh sach chau hoa read from the given file
    """
    print(f"Read file {filename}")
    with open(filename, encoding="utf-8") as file_pointer:
        ds_chau_hoa = next(file_pointer).strip()
    return ds_chau_hoa


def tim_so_chau_hoa_nhieu_nhat(ds_chau_hoa: str) -> int:
    """
    Returns the length of the longest substring in which any 3 consecutive
    characters in the substring are different.
    """
    if len(ds_chau_hoa) < 3:
        return len(ds_chau_hoa)

    do_dai_chau_hoa = [0] * len(ds_chau_hoa)
    do_dai_chau_hoa[0] = 1
    do_dai_chau_hoa[1] = 2

    so_chau_hoa_bo = 0
    for i in range(2, len(ds_chau_hoa)):
        if (
            ds_chau_hoa[i] != ds_chau_hoa[i - so_chau_hoa_bo - 1]
            and ds_chau_hoa[i] != ds_chau_hoa[i - so_chau_hoa_bo - 2]
            and ds_chau_hoa[i - so_chau_hoa_bo - 1]
            != ds_chau_hoa[i - so_chau_hoa_bo - 2]
        ):
            do_dai_chau_hoa[i] = do_dai_chau_hoa[i - 1] + 1
        else:
            so_chau_hoa_bo += 1
            do_dai_chau_hoa[i] = do_dai_chau_hoa[i - 1]
    return do_dai_chau_hoa[-1]


def ghi_file(filename: str, so_chau_hoa: int):
    """
    Write the result into file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(str(so_chau_hoa))
    print(f"Write to file {filename}")


def main():
    """
    Main function
    """
    ds_chau_hoa = doc_file("data/bougain.inp")
    so_chau_hoa = tim_so_chau_hoa_nhieu_nhat(ds_chau_hoa)
    ghi_file("data/bougain.out", so_chau_hoa)


if __name__ == "__main__":
    main()
