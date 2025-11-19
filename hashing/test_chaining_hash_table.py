# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-11-12 09:43:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-11-19 14:09:37
"""
Test ChainingHashTable class
"""
import pytest

from chaining_hash_table import ChainingHashTable


def test_initialization():
    """
    Verifies initialization of a chaining hash table
    """
    ht = ChainingHashTable()
    assert len(ht) == 0
    assert str(ht) == "{}"


def test_insertion():
    """
    Verifies the insertion of an element
    """
    ht = ChainingHashTable()

    # insert an item whose key is not present
    ht.insert("foo", "bar")
    assert len(ht) == 1
    assert ht["foo"] == "bar"

    # overwrite an item whose key already exists
    ht.insert("foo", "baz")
    assert len(ht) == 1
    assert ht["foo"] == "baz"

    # verify that the capacity expands when the load factor exceeds the rehashing threshold
    ht.insert("bar", "foo")
    assert len(ht) == 2
    assert ht.capacity == 5


def test_get_method():
    """
    Verifies the get method returns correct value
    """
    ht = ChainingHashTable()
    ht.insert("foo", "bar")

    # get an item whose key is present
    assert ht.get("foo") == "bar"

    # get an item whose key is not present
    assert ht.get("bar") is None

    # get an item whose key is not present with default value
    assert ht.get("bar", "") == ""


def test_deletion():
    """
    Verifies the deletion functions correctly
    """
    ht = ChainingHashTable()
    ht.insert("foo", "bar")

    # delete an item whose key presents
    del ht["foo"]
    assert "foo" not in ht

    # delete an item whose key isn't present
    with pytest.raises(KeyError):
        del ht["foo"]


def test_items_methods():
    """
    Verifies that the items method returns a list of tuples of key-value
    """
    ht = ChainingHashTable()
    ht.insert("foo", "bar")
    assert ht.items() == [("foo", "bar")]
