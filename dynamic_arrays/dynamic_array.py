# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-10-11 18:05:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-10-14 00:13:08
"""
Dynamic Array
"""
import ctypes
from typing import Any, Generator, Iterable, Optional


class DynamicArray:
    """
    DynamicArray class
    """

    def __init__(
        self, initial: Optional[Iterable[Any]] = None, growth_factor: int = 2
    ) -> None:
        self._growth_factor = growth_factor

        if initial is None:
            self._no_items = 0
            self._capacity = 1
            self._array = self._make_array(self.capacity)
        else:
            data = list(initial)
            capacity = 1
            while capacity < len(data):
                capacity *= growth_factor

            self._no_items = len(data)
            self._capacity = capacity
            self._array = self._make_array(self.capacity)

            for i, value in enumerate(data):
                self._array[i] = value

    def __len__(self) -> int:
        return self._no_items

    def __str__(self) -> str:
        str_items = ", ".join(str(self._array[i]) for i in range(len(self)))
        return f"[{str_items}]"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self)})"

    def __iter__(self) -> Generator[Any, None, None]:
        for i in range(len(self)):
            yield self._array[i]

    def __getitem__(self, index: int) -> Any:
        # Normalize and validate the index provided
        index = self._normalize_index(index)
        self._validate_index(index)

        return self._array[index]

    def __setitem__(self, index: int, value: Any):
        # Normalize and validate the index provided
        index = self._normalize_index(index)
        self._validate_index(index)

        # Assign the item
        self._array[index] = value

    def __delitem__(self, index: int):
        # Normalize and validate the index provided
        index = self._normalize_index(index)
        self._validate_index(index)

        # Shift elements from the index to the end of the array one position to the left
        for i in range(index, len(self) - 1):
            self._array[i] = self._array[i + 1]
        self._array[len(self) - 1] = None  # clear the reference to the last element
        self._no_items -= 1  # update the total number of items
        self._shrink_if_needed()

    @property
    def capacity(self) -> int:
        """
        Returns the capacity of the array.
        """
        return self._capacity

    @property
    def growth_factor(self) -> int:
        """
        Returns the growth factor of the array.
        """
        return self._growth_factor

    def _make_array(self, capacity: int) -> ctypes.Array:
        """
        Returns an array with the size provided.
        """
        # Create an array with a specified capacity, where each item is a Python object
        array_type = capacity * ctypes.py_object
        return array_type()

    def _resize(self, capacity: int):
        """
        Resizes the array to the new capacity.
        """
        # Create a temporary array with new capacity, then copy items to it
        temp_array = self._make_array(capacity)
        for i in range(len(self)):
            temp_array[i] = self._array[i]

        # Assign array to the temporary array, and update the capacity
        self._array = temp_array
        self._capacity = capacity

    def _normalize_index(self, index: int) -> int:
        """
        Returns a non-negative index representing the same position.
        """
        return len(self) + index if index < 0 else index

    def _validate_index(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError("index out of range")

    def _shrink_if_needed(self):
        """
        Shrinks the array when necessary.
        """
        shrink_factor = 1 / (self.growth_factor**2)
        if 0 < len(self) <= int(self.capacity * shrink_factor):
            capacity = max(1, self.capacity // self.growth_factor)
            self._resize(capacity)

    def append(self, item: Any):
        """
        Inserts an item at the end of the array.
        """
        # Expand the array if its capacity reaches limit
        if len(self) == self.capacity:
            self._resize(self.growth_factor * self.capacity)

        # Append the item and update the total number of items
        self._array[len(self)] = item
        self._no_items += 1

    def insert(self, index: int, item: Any):
        """
        Inserts an item to the index provided.

        If the index is less than 0, the item will be inserted at the first position.
        If the index is greater than the length of the array, the item will be inserted
        at the last position.
        """
        # Normalize the index
        index = 0 if index < 0 else index
        index = len(self) if index > len(self) else index

        # Insert the item at the last position
        if index == len(self):
            self.append(item)
            return

        # Expand the array when it reaches its capacity
        if len(self) == self.capacity:
            self._resize(self.growth_factor * self.capacity)

        # Shift elements from index to the end of the array one position to the right
        for i in range(len(self), index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = item  # set the element at the index to the new value
        self._no_items += 1  # update the total number of items

    def remove(self, value: Any):
        """
        Removes the first occurrence of the value.

        Raises ValueError if the value is not present.
        """
        # Find the index of the first occurence of the value in the array
        index = -1
        for i in range(len(self)):
            if self._array[i] == value:
                index = i
                break

        # No matching value was found in the array
        if index == -1:
            raise ValueError(f"{value} not in the array")

        # Found the index of the value in the array
        del self[index]

    def pop(self, index: int = -1) -> Any:
        """
        Removes and returns the item at the specified index (defaults to last).

        Raises IndexError if the index is out of range.
        """
        # Normalize and validate the index provided
        index = self._normalize_index(index)
        self._validate_index(index)

        # Remove and return the item
        value = self._array[index]
        del self[index]
        return value

    def clear(self):
        """
        Removes all items from the array.
        """
        # Clear the references to all elements
        for i in range(len(self)):
            self._array[i] = None

        # Resize the array
        self._no_items = 0
        self._resize(1)

    def find(self, value: Any) -> int:
        """
        Returns the index of the first occurrence of the value.

        Returns -1 when the value is not found in the array.
        """
        for i in range(len(self)):
            if self._array[i] == value:
                return i
        return -1
