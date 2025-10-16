# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-10-12 18:31:07
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-10-16 15:20:16
"""
Test Dynamic Array class
"""
import pytest
from dynamic_array import DynamicArray


@pytest.fixture(name="sample_array")
def create_sample_array() -> DynamicArray:
    """
    Returns the sample dynamic array.
    """
    arr = DynamicArray()
    arr.append(1)
    arr.append(2.2)
    arr.append("foo")
    return arr


def test_array_initialization():
    """
    Verifies initialization of an array.
    """
    arr = DynamicArray()
    assert len(arr) == 0
    assert arr.capacity == 1
    assert arr.growth_factor == 2
    assert str(arr) == "[]"
    assert repr(arr) == "DynamicArray(_no_items=0, _capacity=1, _array=[])"


@pytest.mark.parametrize("items", [(2, "foo"), ("bar", 5, 7)])
def test_append_items_to_array(items):
    """
    Verifies appending items to an array.
    """
    arr = DynamicArray()
    for item in items:
        arr.append(item)
    assert len(arr) == len(items)
    assert str(arr) == f"[{', '.join(str(item) for item in items)}]"


@pytest.mark.parametrize("growth_factor", [3, 5])
def test_array_growth_factor_logic(growth_factor):
    """
    Verifies correct handling of growth factor.
    """
    arr = DynamicArray(growth_factor=growth_factor)
    assert arr.growth_factor == growth_factor

    for i in range(growth_factor + 1):
        arr.append(i)
    assert arr.capacity == growth_factor**2


def test_get_element_by_index(sample_array):
    """
    Checks retrieval of an element by index.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"

    assert arr[0] == 1
    assert arr[1] == 2.2
    assert arr[-1] == "foo"

    with pytest.raises(IndexError, match="index out of range"):
        _ = arr[3]


def test_set_element_at_index(sample_array):
    """
    Checks assignment of an element at a specific index.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"

    arr[0] = -1
    arr[-1] = "bar"

    assert arr[0] == -1
    assert arr[-1] == "bar"

    with pytest.raises(IndexError, match="index out of range"):
        arr[3] = ""


def test_insert_element_at_index(sample_array):
    """
    Checks insertion of an element at a specific index.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"

    arr.insert(1, 3.3)
    assert str(arr) == "[1, 3.3, 2.2, foo]"

    arr.insert(10, "bar")
    assert str(arr) == "[1, 3.3, 2.2, foo, bar]"

    arr.insert(-10, "baz")
    assert str(arr) == "[baz, 1, 3.3, 2.2, foo, bar]"


def test_delete_element_at_index(sample_array):
    """
    Checks deletion of an element at a specific index.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"
    assert arr.capacity == 4

    del arr[0]
    assert str(arr) == "[2.2, foo]"
    assert arr.capacity == 4

    del arr[-1]
    assert str(arr) == "[2.2]"
    assert arr.capacity == 2

    with pytest.raises(IndexError, match="index out of range"):
        del arr[2]


def test_remove_first_occurrence(sample_array):
    """
    Checks removal of the first occurrence of a value.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"

    arr.append(2.2)
    assert str(arr) == "[1, 2.2, foo, 2.2]"

    arr.remove(2.2)
    assert str(arr) == "[1, foo, 2.2]"

    with pytest.raises(ValueError, match="bar not in the array"):
        arr.remove("bar")


def test_pop_at_index(sample_array):
    """
    Checks popping an element at a specific index.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"

    value = arr.pop(1)
    assert value == 2.2
    assert str(arr) == "[1, foo]"

    value = arr.pop(-1)
    assert value == "foo"
    assert str(arr) == "[1]"

    with pytest.raises(IndexError, match="index out of range"):
        _ = arr.pop(1)

    value = arr.pop(0)
    assert value == 1
    assert str(arr) == "[]"


def test_clear_array(sample_array):
    """
    Checks the removal of all elements from the array.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"
    assert arr.capacity == 4

    arr.clear()
    assert len(arr) == 0
    assert str(arr) == "[]"
    assert arr.capacity == 1


def test_find_first_occurrence(sample_array):
    """
    Verifies finding the first occurrence of an item in the array.
    """
    arr = sample_array
    assert str(arr) == "[1, 2.2, foo]"

    arr.append(2.2)
    assert str(arr) == "[1, 2.2, foo, 2.2]"

    index = arr.find(2.2)
    assert index == 1

    index = arr.find("bar")
    assert index == -1


def test_init_with_sequence():
    """
    Verifies initialization with a sequence
    """
    arr = DynamicArray(range(2))
    assert str(arr) == "[0, 1]"
    assert arr.capacity == 2

    arr = DynamicArray([1, 2.2, "foo"])
    assert str(arr) == "[1, 2.2, foo]"
    assert arr.capacity == 4
