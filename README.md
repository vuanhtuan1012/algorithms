# Algorithms  <!-- omit in toc -->

- [Dynamic Arrays](#dynamic-arrays)
  - [Definition](#definition)
  - [Implementation](#implementation)
- [ctypes](#ctypes)
- [Stack Memory vs. Heap Memory](#stack-memory-vs-heap-memory)
- [Hash Usage](#hash-usage)
- [Hash Implementation](#hash-implementation)
- [Prefix Sums](#prefix-sums)
- [Reference](#reference)


## Dynamic Arrays

### Definition

- A **dynamic array** is a data structure that behaves **like a regular array** (*static array, fixed size*) but with one key superpower: it can **automatically resize** itself when it runs out of space.

  For example, `list` in Python, `vector` in C++, `ArrayList` in Java are dynamic arrays.

- **Key features:**
  - **Resizable:** the size of a dynamic array increases (and sometimes decreases) **as needed**.
  - **Contiguous memory:** elements are stored next to each other in memory, so we still get **fast random access** (`O(1)` time to *access an element by index*).

- **How it works:**
  - When created, a dynamic array allocates a temporary array with an intial size (say $capacity = 1$, for example).
  - When we add elements beyond the current capacity:
    - a new larger array is created, *often **double** the previous size* (say $growthFactor = 2$, for example).
    - the old elements are copied into the new array.
    - the old array is freed from memory.
  - When elements are removed, the array may shrink to save memory (*depending on the language and implementation*).
- **How it shrinks:**
  - When the number of elements is less than or equals a certain fraction of the capacity, *often **1/4** of the capacity*, the capacity will be reduced. (say $shrinkFactor = 1/4$).
  - The array will be shrunk to half of its current size.
  - In summary, the shrink factor is defined as $\frac{1}{growthFactor^2}$. The shrink process is triggered when the number of elements is less than or equal to $capacity * shrinkFactor$. When activated, the array shrinks to a new capacity equal to $\frac{capacity}{growthFactor}$.

- **Complexity:**

  | Operation          | Time Complexity |
  |--------------------|-----------------|
  | Access by index    | `O(1)`          |
  | Insert at end      | `O(1)`          |
  | Insert *in middle* | `O(n)`          |
  | Delete at end      | `O(1)`          |
  | Delete *in middle* | `O(n)`          |

### Implementation

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
  - `_make_array`: Creates and returns an array (fixed-size, contiguous memory block) of the given capacity using `ctypes.py_object`.
  - `_resize`: Expands or shrinks the array based on the provided `capacity` value.
  - `_normalize_index`: Returns a non-negative index representing the same position.
  - `_validate_index`: Raises `IndexError` if the index is out of range. Negative indices are not supported.
  - `_shrink_if_needed`: Triggers shrinking when its capacity is greater than or equal to the total number of elements multiplied by the square of the growth factor.
- **Other methods:**
  - `__repr__`: Provides a string representation of the array intended for debugging and development purposes.

## ctypes

- `ctypes` is a powerful **built-in library** that let us work directly with **low-level C data types** and **shared libraries** (`.dll`, `.so`, `.dylib`).
- `ctypes` allows Python code to:
  - **Call C functions:** load shared C libraries and call their function directly from Python.
  - **Use C data types:** create and manipulate low-level data like C `int`, `char`, `double`, `struct`, etc.
  - **Interface with system-level APIs:** useful for interacting with OS libraries or performance-critical native code.
- `ctypes` is useful for:
  - **Preformance:** call optimized C functions directly instead of using pure Python loops.
  - **Low-level memory control:** create dynamic arrays, buffers, or structs.
  - **Interfacing with C/C++ libraries:** use native libraries without wrappers.
  - **Access OS-level APIs:** for example Windows or Unix shared objects.

## Stack Memory vs. Heap Memory

The **stack** stores *function context* and *variable references*, while the **heap** stores *actual objects* and *data that persist beyond a function call*.

| Feature           | Stack                   | Heap                   |
|-------------------|-------------------------|------------------------|
| Purpose           | Store *temporary data* (function calls, local variables) | Store *dynamic data* (objects, arrays, data that changes size) |
| Managed by        | The compiler/runtime automatically                     | The programmer or garbage collector                |
| Memory allocation | Fixed-size, fast (**LIFO order**)                      | Flexible                                           |
| Lifetime          | Exists only while the function is running              | Exists until explecitly freed or garbage collected |
| Speed             | Very fast                                              | Slow due to manual management                      |
| Size limit        | Small, can overflow                                    | Large, only limited by system memory               |

*For example*, consider a function that assigns a local variable to a list:
- When the function is called, the *local variable name* is stored in the **stack frame**, while the *actual list object* is allocated in the **heap**.
- Once the function terminates, the **stack frame is destroyed**, and the *variable name* inside the function disappears. However, the *list object* remains in the **heap**, now without any references pointing to it. At this point, it becomes **eligible for garbage collection**.
- When the garbage collector runs, it will detect the unreferenced list and free the associated memory.

```python
def memo():
  x = [1, 2, 3]
memo()
```

**In Python**, all objects (`int`, `str`, `list`, `dict`, `class`, etc.) are **heap-allocated** (live on the heap). The **stack** only keeps *references* to those heap objects and manages *function calls*.

What actually happens when we write `x = 10` ?
- Python checks whether an integer object representing `10` already exists.
- **If yes**, it reuse it. **If not**, it creates a new on on the **heap**.
- The variable name `x` (lives on the **stack**) simply **points to** that object on the heap.

```python
x = 10
y = 10
print(x is y)  # True
```

**Useful functions:**
- `id`: returns **the unique identity** of an object, which in CPython, is its memory address in the **heap**.

  It can be used to check whether different variable names point to the same object, or to explore object mutability and identity-related behavior.
- `sys.getrefcount`: returns **the number of references** that currently held to an object. **Note that** calling this function **temporarily adds one reference** to the object (as its argument), so the returned count is **one higher** than the actual number.

  Every object in CPython has a reference counter, the count of how many variables, containers, or temporary expressions refer to it.

  When this count drops to **zero**, the garbage collector frees the object from the heap.

- `sys.getsizeof`: returns **the size** of an object in bytes, including its metadata on the heap.

  Note that `sys.getsizeof` returns the size of the object itself in bytes, but does **not include** the size of any objects it references.

  *For example*, in Python, a list object is stored on the heap and contains metadata such as capacity and size, along with an array of pointers to its elements. Each pointer refers to a separate object, also stored on the heap. `sys.getsizeof` reports the size of the list structure itself, not the combined size of its elements.

## Hash Usage

:walking: TODO

## Hash Implementation

:walking: TODO

## Prefix Sums

:walking: TODO

## Reference

1. Course [CodeLearn - Thuật toán căn bản](https://codelearn.io/learning/thuat-toan-can-ban).
2. Book [Nguyễn Tấn Trần Minh Khang - 1000 Bài tập lập trình](high_school/books/Nguyen_Tan_Tran_Minh_Khang_1000_bai_tap_lap_trinh.pdf).
3. Đề [December 21, 2024](high_school/books/DieuChinh_28_De_HSG_Huyen_TinTHCS.pdf).
4. Đề [December 28, 2024](high_school/books/De_2024_12_28.pdf).
5. [NeetCode Roadmap](https://neetcode.io/roadmap)
