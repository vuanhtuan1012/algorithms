# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-10-19 20:43:23
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-10-20 09:32:42
import sys
from time import perf_counter
from prettytable import PrettyTable
from dynamic_array import DynamicArray


def show_performance():
    """
    Show performance of DynamicArray and List
    """
    # Define table
    table = PrettyTable()
    table.field_names = ["Object", "Size", "Time to init (seconds)", "Memory needed (bytes)"]
    table.align["Object"] = "l"
    for col in ("Size", "Time to init (seconds)", "Memory needed (bytes)"):
        table.align[col] = "r"

    for i in range(5):
        no_items = 10**i

        # Dynamic Array
        start = perf_counter()
        arr = DynamicArray(range(no_items))
        end = perf_counter()
        table.add_row(["DynamicArray", no_items, round(end - start, 6), sys.getsizeof(arr)])

        # List
        start = perf_counter()
        lst = list(range(no_items))
        end = perf_counter()
        table.add_row(["List", no_items, round(end - start, 6), sys.getsizeof(lst)])

    print(table)


if __name__ == "__main__":
    show_performance()
