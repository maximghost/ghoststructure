import pytest

from ghoststructure.dynamic_array import DynamicArray


def test_new_array_is_empty() -> None:
    array = DynamicArray[int]()
    assert len(array) == 0


def test_new_array_starts_with_a_small_reserved_capacity() -> None:
    array = DynamicArray[int]()
    assert array.capacity == 4


def test_append_adds_items_in_order() -> None:
    array = DynamicArray[str]()
    array.append("a")
    array.append("b")
    assert len(array) == 2
    assert array[0] == "a"
    assert array[1] == "b"


def test_array_can_be_built_from_an_iterable() -> None:
    array = DynamicArray([10, 20, 30])
    assert len(array) == 3
    assert array[2] == 30


def test_capacity_doubles_when_the_block_is_full() -> None:
    array = DynamicArray([1, 2, 3, 4])
    assert array.capacity == 4
    array.append(5)
    assert array.capacity == 8
    assert [array[i] for i in range(5)] == [1, 2, 3, 4, 5]


def test_negative_index_counts_from_the_end() -> None:
    array = DynamicArray(["a", "b", "c"])
    assert array[-1] == "c"
    assert array[-3] == "a"


@pytest.mark.parametrize("index", [3, 100, -4])
def test_out_of_range_index_raises_index_error(index: int) -> None:
    array = DynamicArray(["a", "b", "c"])
    with pytest.raises(IndexError):
        array[index]
