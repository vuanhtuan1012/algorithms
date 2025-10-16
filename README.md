# Algorithms  <!-- omit in toc -->

- [Arrays \& Hashing](#arrays--hashing)
  - [Dynamic Arrays](#dynamic-arrays)
    - [Definition](#definition)
    - [Implementation](#implementation)
  - [Stack Memory vs. Heap Memory](#stack-memory-vs-heap-memory)
  - [Hash Usage](#hash-usage)
  - [Hash Implementation](#hash-implementation)
  - [Prefix Sums](#prefix-sums)
- [Reference](#reference)


## Arrays & Hashing

### Dynamic Arrays

#### Definition

- A **dynamic array** is a data structure that behaves **like a regular array** (*static array, fixed size*) but with one key superpower: it can **automatically resize** itself when it runs out of space.

  For example, `list` in Python, `vector` in C++, `ArrayList` in Java are dynamic arrays.

- **Key features:**
  - **Resizable:** the size of a dynamic array increases (and sometimes decreases) **as needed**.
  - **Contiguous memory:** elements are stored next to each other in memory, so we still get **fast random access** (`O(1)` time to *access an element by index*).

- **How it works:**
  - When created, a dynamic array allocates a temporary array with an intial size (say $capacity = 1$, for example).
  - When we add elements beyond the current capacity:
    - a new larger array is created, *often **double** the previous size* (say $growth\_ factor = 2$, for example).
    - the old elements are copied into the new array.
    - the old array is freed from memory.
  - When elements are removed, the array may shrink to save memory (*depending on the language and implementation*).
- **How it shrinks:**
  - When the number of elements is less than or equals a certain fraction of the capacity, *often **1/4** of the capacity*, the capacity will be reduced. (say $shrink\_factor = 1/4$).
  - The array will be shrunk to half of its current size.
  - In summary, the shrink factor is defined as $\frac{1}{growth\_factor^2}$. The shrink process is triggered when the number of elements is less than or equal to $capacity * shrink\_factor$. When activated, the array shrinks to a new capacity equal to $\frac{capacity}{growth\_factor}$.

- **Complexity:**

  | Operation          | Time Complexity |
  |--------------------|-----------------|
  | Access by index    | `O(1)`          |
  | Insert at end      | `O(1)`          |
  | Insert *in middle* | `O(n)`          |
  | Delete at end      | `O(1)`          |
  | Delete *in middle* | `O(n)`          |

#### Implementation

The `DynamicArray` class includes the attributes and methods listed below.

- **Attributes:**
  - `_growth_factor` (*protected*): Determines **how much the array grows** when its capacity is reached.
  - `_no_items` (*protected*): Represents the **current number of elements** stored in the array.
  - `_capacity` (*protected*): Indicates **how many elements the array can hold** before resizing.
  - `_array` (*protected*): An array composed of Python objects used to **store the array's contents**.
  - `growth_factor` (*read only*): Exposes the array's growth factor without allowing unintended changes.
  - `capacity` (*read only*): Lets users access the array's capacity without risking unintended changes.
- **Essential dunder methods:**
  - `__init__`: **Constructor method** for initializing. This function accepts two **optional parameters**, an initial sequence (default is `None`) and a growth factor (default is `2`).
  - `__len__`: Returns the current total number of elements in the array, the **array's length**. It's called by the `len` function.
  - `__str__`: Provides a **readable string** version of the array, making it easy to display. It's called by `str` or `print` function.
  - `__iter__`: Enables **iteration** over the array's elements using the `in` operator.
  - `__getitem__`: Enables **indexed access** to array elements, support negative indices, and raises `IndexError` for out of range values.
  - `__setitem__`: Allows **assignment to a specific index** in the array, including negative indices. Raises `IndexError` for invalid indices.
  - `__delitem__`: Enables **deletion by index**, including negative values. Raises `IndexError` if out of range and **shrinks the array if necessary**. It's called by the `del` keyword.
- **Regular methods:**
  - `append`: Inserts an item at the end of the array.
  - `insert`: Inserts an item to the index provided.
    - If the index is less than `0`, the item will be inserted at the first position.
    - If the index is greater than the length of the array, the item will be inserted at the last position.
  - `remove`: Removes the first occurrence of the value provided. Raises `ValueError` if the value is not present.
  - `pop`: Deletes and returns the item at the specified index (last by default). Supports negative indexing and raises `IndexError` if the index is out of range.
  - `clear`: Removes all items from the array.
  - `find`: Finds the index of the first occurrence of the value, returning `-1` if it's not present.
- **Protected methods:**
  - `_make_array`: Creates and returns an array with the given size.
  - `_resize`: Expands or shrinks the array based on the provided `capacity` value.
  - `_normalize_index`: Returns a non-negative index representing the same position.
  - `_validate_index`: Raises `IndexError` if the index is out of range. Negative indices are not supported.
  - `_shrink_if_needed`: Triggers shrinking when its capacity is greater than or equal to the total number of elements multiplied by the square of the growth factor.
- **Other methods:**
  - `__repr__`: Provides a string representation of the array intended for debugging and development purposes.


### Stack Memory vs. Heap Memory

:running: TODO

### Hash Usage

:walking: TODO

### Hash Implementation

:walking: TODO

### Prefix Sums

:walking: TODO

## Reference

1. Course [CodeLearn - Thuật toán căn bản](https://codelearn.io/learning/thuat-toan-can-ban).
2. Book [Nguyễn Tấn Trần Minh Khang - 1000 Bài tập lập trình](high_school/books/Nguyen_Tan_Tran_Minh_Khang_1000_bai_tap_lap_trinh.pdf).
3. Đề [December 21, 2024](high_school/books/DieuChinh_28_De_HSG_Huyen_TinTHCS.pdf).
4. Đề [December 28, 2024](high_school/books/De_2024_12_28.pdf).
5. [NeetCode Roadmap](https://neetcode.io/roadmap)
