"""A dynamic array: the structure behind Python's ``list``."""

from collections.abc import Iterable
from typing import cast

_INITIAL_CAPACITY = 4
_GROWTH_FACTOR = 2


class DynamicArray[T]:
    """A resizable array with amortized O(1) appends.

    Elements live in a fixed-size block of memory. When the block is full, a
    block twice as large is allocated and every element is copied into it.
    """

    def __init__(self, items: Iterable[T] = ()) -> None:
        """Create an array, optionally filled with ``items``."""
        self._capacity = _INITIAL_CAPACITY
        self._size = 0
        self._block: list[T | None] = [None] * self._capacity
        for item in items:
            self.append(item)

    @property
    def capacity(self) -> int:
        """Number of slots reserved in memory (always >= ``len(self)``)."""
        return self._capacity

    def __len__(self) -> int:
        """Return the number of elements stored. O(1)."""
        return self._size

    def append(self, item: T) -> None:
        """Add ``item`` at the end. Amortized O(1)."""
        if self._size == self._capacity:
            self._resize(self._capacity * _GROWTH_FACTOR)
        self._block[self._size] = item
        self._size += 1

    def __getitem__(self, index: int) -> T:
        """Return the element at ``index`` (negative indexes allowed). O(1).

        Raises:
            IndexError: If ``index`` is out of range.
        """
        if index < 0:
            index += self._size
        if not 0 <= index < self._size:
            raise IndexError("DynamicArray index out of range")
        # Every slot below _size holds a real item, never the None placeholder.
        return cast("T", self._block[index])

    def _resize(self, new_capacity: int) -> None:
        """Move every element to a new block of ``new_capacity`` slots. O(n)."""
        new_block: list[T | None] = [None] * new_capacity
        for i in range(self._size):
            new_block[i] = self._block[i]
        self._block = new_block
        self._capacity = new_capacity
