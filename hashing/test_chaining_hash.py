# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-11-12 09:43:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-11-12 10:42:40
"""
Test ChainingHash class
"""
import pytest

from chaining_hash import ChainingHash


def test_initialization():
    """
    Verifies initialization of a chaining hash
    """
    ch = ChainingHash()
    assert len(ch) == 0
    assert str(ch) == "{}"


def test_insertion():
    """
    Verifies the insertion of an element
    """
    ch = ChainingHash()

    # insert an item whose key is not present
    ch.insert("foo", "bar")
    assert len(ch) == 1
    assert ch["foo"] == "bar"

    # overwrite an item whose key already exists
    ch.insert("foo", "baz")
    assert len(ch) == 1
    assert ch["foo"] == "baz"

    # verify the capacity is updated
    ch.insert("bar", "foo")
    assert len(ch) == 2
    assert ch.capacity == 5


def test_get_method():
    """
    Verifies the get method returns correct value
    """
    ch = ChainingHash()
    ch.insert("foo", "bar")

    # get an item whose key is present
    assert ch.get("foo") == "bar"

    # get an item whose key is not present
    assert ch.get("bar") is None

    # get an item whose key is not present with default value
    assert ch.get("bar", "") == ""


def test_deletion():
    """
    Verifies the deletion functions correctly
    """
    ch = ChainingHash()
    ch.insert("foo", "bar")

    # delete an item whose key presents
    del ch["foo"]
    assert "foo" not in ch

    # delete an item whose key isn't present
    with pytest.raises(KeyError):
        del ch["foo"]


def test_items_methods():
    """
    Verifies that the items method returns a list of tuples of key-value
    """
    ch = ChainingHash()
    ch.insert("foo", "bar")
    assert ch.items() == [("foo", "bar")]
