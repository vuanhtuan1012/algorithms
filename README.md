# Algorithms  <!-- omit in toc -->

- [Arrays \& Hashing](#arrays--hashing)
  - [Dynamic Arrays](#dynamic-arrays)
  - [Stakc Memory vs. Heap Memory](#stakc-memory-vs-heap-memory)
  - [Hash Usage](#hash-usage)
  - [Hash Implementation](#hash-implementation)
  - [Prefix Sums](#prefix-sums)
- [Reference](#reference)


## Arrays & Hashing

### Dynamic Arrays

- A **dynamic array** is a data structure that behaves **like a regular array** (*static array, fixed size*) but with one key superpower: it can **automatically resize** itself when it runs out of space.
- For example, `list` in Python, `vector` in C++, `ArrayList` in Java are dynamic arrays.

- **Key features:**
  - **Resizable:** the size of a dynamic array increases (and sometimes decreases) as needed.
  - **Contiguous memory:** elements are stored next to each other in memory, so we still get **fast random access** (`O(1)` time to *access an element by index*).

- **How it works:**
  - When created, a dynamic array allocates a temporary array with an intial size (*say capacity = 1, for example*).
  - When we add elements beyond the current capacity:
    - a new larger array is created, *often **double** the previous size*.
    - the old elements are copied into the new array.
    - the old array is freed from memory.
  - When elements are removed, the array may shrink to save memory (*depending on the language and implementation*).

- **Complexity:**

  | Operation          | Time Complexity |
  |--------------------|-----------------|
  | Access by index    | `O(1)`          |
  | Insert at end      | `O(1)`          |
  | Insert *in middle* | `O(n)`          |
  | Delete at end      | `O(1)`          |
  | Delete *in middle* | `O(n)`          |

- **Implementation:**


### Stakc Memory vs. Heap Memory

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
