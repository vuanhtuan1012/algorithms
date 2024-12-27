# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-12-26 12:47:18
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-12-27 10:20:40

"""
Đề số 28 - Bài 4 - Trang 177

Ở một quầy tạp hoá, giá bán lẻ mỗi chiếc bút là m.
Tuy nhiên, cửa hàng có chương trình khuyến mãi là
cứ mua n chiếc bút thì sẽ được cửa hàng tặng thêm một chiếc bút.
Viết chương trình nhập 4 số nguyên dương m, n, p, k từ bàn phím. In ra màn hình:
- Số tiền ít nhất phải trả để được số bút tặng thêm là p (S).
- Số tiền phải trả để có được k chiếc bút (T).

Ví dụ: với m = 6, n = 5, p = 3, k = 20 thì in ra kết quả: S = 90, T = 102
"""
from typing import Tuple


def nhap_lieu() -> Tuple[int, int, int, int]:
    """
    Returns price, promotion threshold, number of extra pens, number of purchased pens
    """
    gia_ban = int(input("Nhap gia ban le: m = "))
    nguong_km = int(input("Nhap nguong khuyen mai: n = "))
    so_but_km = int(input("Nhap so but khuyen mai: p = "))
    so_but_can_mua = int(input("Nhap so but can mua: k = "))
    return gia_ban, nguong_km, so_but_km, so_but_can_mua


def tinh_so_tien_it_nhat_de_co_n_but_km(
    gia_ban: int, nguong_km: int, so_but_km: int
) -> int:
    """
    Returns min cost to get n promotion pens
    """
    return nguong_km * so_but_km * gia_ban


def tinh_so_tien_de_mua_n_but(gia_ban: int, nguong_km: int, so_but_can_mua: int) -> int:
    """
    Returns cost to get n pens
    """
    so_but_km = int(so_but_can_mua / (nguong_km + 1))
    so_but_tt = so_but_can_mua - so_but_km
    return so_but_tt * gia_ban


def dry_test():
    """
    Dry test
    """
    gia_ban, nguong_km, so_but_km, so_but_can_mua = 6, 5, 3, 20
    print(
        f"So tien it nhat phai tra de duoc {so_but_km} but tang them la: S = "
        f"{tinh_so_tien_it_nhat_de_co_n_but_km(gia_ban, nguong_km, so_but_km)}"
    )
    print(
        f"So tien de mua {so_but_can_mua} but la: T = "
        f"{tinh_so_tien_de_mua_n_but(gia_ban, nguong_km, so_but_can_mua)}"
    )


def main():
    """
    Main function
    """
    gia_ban, nguong_km, so_but_km, so_but_can_mua = nhap_lieu()
    print(
        f"So tien it nhat phai tra de duoc {so_but_km} but tang them la: S = "
        f"{tinh_so_tien_it_nhat_de_co_n_but_km(gia_ban, nguong_km, so_but_km)}"
    )
    print(
        f"So tien de mua {so_but_can_mua} but la: T = "
        f"{tinh_so_tien_de_mua_n_but(gia_ban, nguong_km, so_but_can_mua)}"
    )


if __name__ == "__main__":
    main()
