# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-03-10 18:55:38
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-03-11 16:41:11

"""
Bài 1. Trò chơi
"""
from typing import List, Tuple


def doc_file(filename: str) -> List[Tuple[int, int, int, int]]:
    """
    Returns list of numbers read from file
    """
    games = []
    with open(filename, encoding="utf-8") as file_pointer:
        for i, line in enumerate(file_pointer):
            if i == 0:
                continue
            numbers = tuple(map(int, line.strip().split()))
            games.append(numbers)
    return games


def ghi_file(filename: str, winners: List[str]):
    """
    Write winners into file
    """
    with open(filename, "w", encoding="utf-8") as file_pointer:
        file_pointer.write("\n".join(winners))
    print(f"Data is written to file {filename}")


def is_prime(number: int) -> bool:
    """
    Returns True if number is prime, otherwise False
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_winner(a: int, b: int, c: int, d: int) -> str:
    """
    Returns "Tam" if If there exists a number in the interval a, b
    such that its sum with every number in the interval c, d isn't a prime number.
    Otherwise, "Cam"
    """
    for i in range(a, b + 1):
        found_prime = False
        for j in range(c, d + 1):
            if is_prime(i + j):
                found_prime = True
                break
        if not found_prime:
            return "Tam"
    return "Cam"


def main():
    """
    Main function
    """
    games = doc_file("data/game.inp")
    winners = []
    for numbers in games:
        winner = find_winner(*numbers)
        winners.append(winner)
    ghi_file("data/game.out", winners)


if __name__ == "__main__":
    main()
