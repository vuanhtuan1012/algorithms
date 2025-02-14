# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-02-09 23:54:26
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-02-14 23:43:40

"""
Trong thế giới cờ vua, con tượng không thích con tượng khác.
Trong thực tế, khi 2 con tượng cùng đứng chung 1 đường chéo,
chúng lập tức di chuyển tới hai đầu của đường chéo đó.

Cho vị trí ban đầu của hai con tượng trên bàn cờ vua.
Hãy tính toán vị trí của chúng sau khi di chuyển tới hai đầu của đường chéo
mà chúng đang đứng. Kết quả trả về luôn xếp theo thứ tự alphabeta.
Nhớ rằng con tượng sẽ không di chuyển
trừ khi chúng đứng chung trên một đường chéo.

Ví dụ:
- bishopDiagonal("d7", "f5") = ["c8", "h3"].
- bishopDiagonal("d8", "b5") = ["b5", "d8"].
"""
from typing import Tuple


def square_to_coordinate(square: str) -> Tuple[int, int]:
    """
    Returns the coordinate of the given square
    """
    return [ord(square[0].upper()), int(square[1])]


def is_on_same_diagonal(first_bishop: str, second_bishop) -> bool:
    """
    Returns True if the two given bishops are on the same diagonal, otherwise False
    """
    x0, y0 = square_to_coordinate(first_bishop)
    x1, y1 = square_to_coordinate(second_bishop)
    return abs(x0 - x1) == abs(y0 - y1)


def coordinate_to_square(x: int, y: int) -> str:
    """
    Returns the square of the given coordinate
    """
    return f"{chr(x)}{y}"


def move_bishop(bishop: str, x_delta: int, y_delta: int) -> str:
    """
    Returns the given bishop to one end of its diagonals
    """
    x, y = square_to_coordinate(bishop)
    x_limit = ord("H") if x_delta == 1 else ord("A")
    y_limit = 8 if y_delta == 1 else 1
    while x != x_limit and y != y_limit:
        x += x_delta
        y += y_delta
    new_position = coordinate_to_square(x, y)
    return new_position.lower() if bishop.islower() else new_position


def move_bishops(first_bishop: str, second_bishop: str) -> Tuple[str, str]:
    """
    Returns positions of the two given bishops after their moves
    """
    # swap bishops if needed to ensure they're sorted in alphabetic order
    if first_bishop >= second_bishop:
        first_bishop, second_bishop = second_bishop, first_bishop

    # don't move if they're not on the same diagonal
    if not is_on_same_diagonal(first_bishop, second_bishop):
        return first_bishop, second_bishop

    # bishops are on the same diagonal
    x0, y0 = square_to_coordinate(first_bishop)
    x1, y1 = square_to_coordinate(second_bishop)
    x_delta = 1 if x0 > x1 else -1
    y_delta = 1 if y0 > y1 else -1

    # move bishops to ends of the diagonal
    first_bishop = move_bishop(first_bishop, x_delta, y_delta)
    second_bishop = move_bishop(second_bishop, -x_delta, -y_delta)

    return first_bishop, second_bishop


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("d7", "f5", ("c8", "h3")),
        ("d8", "b5", ("b5", "d8")),
        ("a1", "h8", ("a1", "h8")),
    ]
    for i, (first_bishop, second_bishop, ground_truth) in enumerate(
        test_cases, start=0
    ):
        result = move_bishops(first_bishop, second_bishop)
        print(f"Test case {i}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
