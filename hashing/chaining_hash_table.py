# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-11-10 15:45:14
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-11-15 09:53:36
"""
Chaining Hash Table
"""
from typing import Any, Generator
from collections.abc import Hashable


class ChainingHashTable:
    """
    ChainingHashTable class
    """

    def __init__(self) -> None:
        self._no_items = 0
        self._capacity = 2
        self._table = [[] for _ in range(self._capacity)]

    def __len__(self) -> int:
        return self._no_items

    def __str__(self) -> str:
        representation = ", ".join(
            f"{key}: {value}" for bucket in self._table for key, value in bucket
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
        if key not in self:
            raise KeyError(key)
        return next(val for k, val in self.items() if k == key)

    def __setitem__(self, key: Hashable, value: Any):
        self.insert(key, value)

    def __delitem__(self, key: Hashable):
        idx = self.hash(key)
        bucket = self._table[idx]

        try:
            bucket_idx = next((idx for idx, (k, _) in enumerate(bucket) if k == key))
        except StopIteration as exc:
            raise KeyError(key) from exc

        del bucket[bucket_idx]
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
        Returns the load factor of the table
        """
        return self._no_items / self._capacity

    @property
    def rehashing_threshold(self) -> float:
        """
        Defines the rehashing threshold
        """
        return 0.7

    def _is_prime(self, number: int) -> bool:
        """
        Determines whether the given number is prime. Returns True if it is, False otherwise
        """
        if number < 2:
            return False

        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def _update_capacity(self):
        """
        Updates the capacity to the next prime number greater than twice its current value
        """
        capacity = self._capacity * 2
        while not self._is_prime(capacity):
            capacity += 1
        self._capacity = capacity

    def _rehash_if_needed(self):
        """
        Rehashes the current object when necessary
        """
        # check pre-condition
        if self.load_factor < self.rehashing_threshold:
            return

        self._update_capacity()
        # extend the table
        table = [[] for _ in range(self._capacity)]
        for key, value in self.items():
            idx = self.hash(key)
            table[idx].append((key, value))
        self._table = table

    def hash(self, key: Hashable) -> int:
        """
        Returns hashed key
        """
        return hash(key) % self._capacity

    def insert(self, key: Hashable, value: Any):
        """
        Inserts a pair of key value to the table

        If the provided key already presents in the table, overwrite the current value
        """
        idx = self.hash(key)
        bucket = self._table[idx]

        # looking for the index of the provided key in the bucket
        bucket_idx = next((i for i, (k, _) in enumerate(bucket) if k == key), -1)
        if bucket_idx >= 0:  # present: overwrite the current item
            bucket[bucket_idx] = (key, value)
            return

        # not present: add new item
        bucket.append((key, value))
        self._no_items += 1
        self._rehash_if_needed()

    def get(self, key: Hashable, default: Any = None) -> Any:
        """
        Returns the value of the provided key

        If the key doesn't present in the table, the default value is returned
        """
        idx = self.hash(key)
        bucket = self._table[idx]
        return next((value for k, value in bucket if k == key), default)

    def items(self) -> list[tuple[Hashable, Any]]:
        """
        Returns the list of items in the table
        """
        return [item for bucket in self._table for item in bucket]
