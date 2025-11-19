# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-11-15 13:44:51
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-11-19 14:07:21
"""
Test LinearProbingHashTable
"""
from typing import Any
import pytest
from linear_probing_hash_table import LinearProbingHashTable


@pytest.fixture(name="ht")
def init_hash_table():
    """
    Returns a new instance of the hash table
    """
    return LinearProbingHashTable()


def test_initialization(ht: LinearProbingHashTable):
    """
    Verifies initialization of a linear probing hash table
    """
    assert ht.capacity == 2
    assert len(ht) == 0
    assert str(ht) == "{}"


def test_insertion(ht: LinearProbingHashTable):
    """
    Verifies the insertion of an element
    """
    # insert an item whose key is not present
    ht.insert("foo", "bar")
    assert len(ht) == 1
    assert ht["foo"] == "bar"

    # overwrite an item whose key already exists
    ht.insert("foo", "baz")
    assert len(ht) == 1
    assert ht["foo"] == "baz"

    # verify that the capacity is doubled when the load factor exceeds the rehashing threshold
    ht.insert("bar", "foo")
    assert len(ht) == 2
    assert ht.capacity == 4


def test_get_method(ht: LinearProbingHashTable):
    """
    Verifies the get method returns correct value
    """
    ht.insert("foo", "bar")

    # get an item whose key is present
    assert ht.get("foo") == "bar"

    # get an item whose key is not present
    assert ht.get("bar") is None

    # get an item whose key is not present with default value
    assert ht.get("bar", "") == ""


def test_deletion(ht: LinearProbingHashTable):
    """
    Verifies the deletion functions correctly
    """
    ht.insert("foo", "bar")

    # delete an item whose key presents
    assert "foo" in ht
    del ht["foo"]
    assert "foo" not in ht

    # delete an item whose key isn't present
    with pytest.raises(KeyError):
        del ht["foo"]


def test_items_method(ht: LinearProbingHashTable):
    """
    Verifies that the items method returns a list of tuples of key-value
    """
    assert ht.items() == []
    ht.insert("foo", "bar")
    assert ht.items() == [("foo", "bar")]


class FakeKey():
    """
    FakeKey class forces all instances to have the same hash value to produce collisions
    """
    def __init__(self, value: Any) -> None:
        self.value = value

    def __hash__(self) -> int:
        """
        Returns a constant value so all instances share the same hash value, causing collisions
        """
        return 0

    def __eq__(self, other: object) -> bool:
        return isinstance(other, FakeKey) and self.value == other.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"


def test_collisions(ht: LinearProbingHashTable):
    """
    Verifies that collisions are properly handled
    """
    k1, k2, k3 = FakeKey("a"), FakeKey("b"), FakeKey("c")
    for key in (k1, k2, k3):
        ht.insert(key, f"{key.value}")

    assert ht.table[:3] == [(k1, k1.value), (k2, k2.value), (k3, k3.value)]


def test_tombstone(ht: LinearProbingHashTable):
    """
    Verifies that tombstones function correctly
    """
    k1, k2, k3 = FakeKey("a"), FakeKey("b"), FakeKey("c")
    for key in (k1, k2, k3):
        ht.insert(key, f"{key.value}")

    # verify that a tombstone is created when an element is deleted
    del ht[k2]
    assert ht.table[1] is ht.tombstone

    # verify that the get method correctly handles tombstones when searching for values
    assert ht.get(k3) == "c"

    # verify that tombstones are reused when inserting a new element with the same hash value
    k4 = FakeKey("d")
    ht.insert(k4, k4.value)
    assert ht.table[1] == (k4, k4.value)
    assert ht.get(k4) == k4.value
    assert ht.tombstone not in ht.table
