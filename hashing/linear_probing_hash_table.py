# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-11-14 11:19:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-11-19 06:01:03
"""
Linear Probing Hash Table
"""
from collections.abc import Hashable
from typing import Any, Generator, Optional, Union

HashTableElement = Union[None, object, tuple[Hashable, Any]]


class LinearProbingHashTable:
    """
    LinearProbingHashTable class
    """

    def __init__(self) -> None:
        self._no_items = 0
        self._capacity = 2
        self._table: list[HashTableElement] = [None] * self._capacity
        self._tombstone = object()

    def __len__(self) -> int:
        return self._no_items

    def __str__(self) -> str:
        # pylint: disable=E1136
        representation = ", ".join(
            f"{item[0]}: {item[1]}" for item in self._table if isinstance(item, tuple)
        )
        return f"{{{representation}}}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(_no_items={self._no_items}, "
            f"_capacity={self._capacity}, _table={self._table})"
        )

    def __iter__(self) -> Generator[Any, None, None]:
        for key, _ in self.items():
            yield key

    def __getitem__(self, key: Hashable) -> Any:
        idx = self._find_index(key)
        if idx is None:
            raise KeyError(key)
        return self._table[idx][1]  # type: ignore

    def __setitem__(self, key: Hashable, value: Any):
        self.insert(key, value)

    def __delitem__(self, key: Hashable):
        idx = self._find_index(key)
        if idx is None:
            raise KeyError(key)

        self._table[idx] = self._tombstone
        self._no_items -= 1

    @property
    def capacity(self) -> int:
        """
        Returns the capacity of the table
        """
        return self._capacity

    @property
    def load_factor(self) -> float:
        """
        Return the load factor of the table
        """
        return self._no_items / self.capacity

    @property
    def rehasing_threshold(self) -> float:
        """
        Defines the rehasing threshold
        """
        return 0.7

    @property
    def tombstone(self) -> object:
        """
        Returns the tombstone
        """
        return self._tombstone

    @property
    def table(self) -> list[HashTableElement]:
        """
        Returns the table
        """
        return self._table

    def _find_index(self, key: Hashable) -> Optional[int]:
        """
        Returns the index of the given key in the table, or None if the key is not found
        """
        idx = self.hash(key)
        for _ in range(self.capacity):
            # the given key isn't in the table
            if self._table[idx] is None:
                return None

            # found index of the given key
            if isinstance(self._table[idx], tuple) and self._table[idx][0] == key:  # type: ignore
                return idx

            idx = (idx + 1) % self.capacity
        return None

    def _find_available_index(self, key: Hashable) -> int:
        """
        Returns the available index in the table where the given key can be inserted
        """
        idx = self.hash(key)
        first_tombstone_idx = None
        for _ in range(self.capacity):
            if self._table[idx] is None:
                return first_tombstone_idx if first_tombstone_idx is not None else idx
            if isinstance(self._table[idx], tuple) and self._table[idx][0] == key:  # type: ignore
                return idx
            if self._table[idx] is self._tombstone and first_tombstone_idx is None:
                first_tombstone_idx = idx
            idx = (idx + 1) % self.capacity
        return idx

    def _rehash_if_needed(self):
        """
        Rehashes the current object when necessary
        """
        # check pre-condition
        if self.load_factor < self.rehasing_threshold:
            return

        table = self._table
        self._no_items = 0
        self._capacity *= 2
        self._table = [None] * self.capacity
        for element in table:
            if isinstance(element, tuple):
                self.insert(*element)  # pylint: disable=E1133

    def hash(self, key: Hashable) -> int:
        """
        Returns hashed key
        """
        return hash(key) % self.capacity

    def insert(self, key: Hashable, value: Any):
        """
        Inserts a pair of key value to the table

        If the provided key already presents in the table, overwrite the current value
        """
        idx = self._find_available_index(key)

        if not isinstance(self._table[idx], tuple):  # a new pair will be added
            self._no_items += 1

        self._table[idx] = (key, value)
        self._rehash_if_needed()

    def get(self, key: Hashable, default: Any = None) -> Any:
        """
        Returns the value of the provided key

        If the key doesn't present in the table, the default value is returned
        """
        idx = self._find_index(key)
        return default if idx is None else self._table[idx][1]  # type: ignore

    def items(self) -> list[tuple[Hashable, Any]]:
        """
        Returns the list of items in the table
        """
        return [item for item in self._table if item not in (None, self._tombstone)]  # type: ignore
