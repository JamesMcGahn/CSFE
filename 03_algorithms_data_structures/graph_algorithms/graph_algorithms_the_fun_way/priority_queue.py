from __future__ import annotations
from typing import Any, Union


class HeapItem:
    def __init__(self, value: Any, priority: float):
        self.value = value
        self.priority = priority

    def __lt__(self, other: HeapItem):
        return self.priority < other.priority

    def __gt__(self, other: HeapItem):
        return self.priority > other.priority


class PriorityQueue:
    def __init__(self, size: int = 100, min_heap: bool = False):
        self.array_size: int = size
        self.heap_array: list[HeapItem | None] = [None] * size
        self.last_index: int = 0
        self.is_min_heap: bool = min_heap
        self.indices: dict[Any, int] = {}

    def size(self) -> int:
        return self.last_index

    def is_empty(self) -> bool:
        return self.last_index == 0

    def in_queue(self, value: Any) -> bool:
        return value in self.indices

    def get_priority(self, value: Any) -> Union[float, None]:
        if value not in self.indices:
            return None
        ind: int = self.indices[value]
        return self.heap_array[ind].priority

    def _elements_inverted(self, parent: int, child: int) -> bool:
        if parent < 1 or parent > self.last_index:
            return False
        if child < 1 or child > self.last_index:
            return False

        # note HeapItem gt lt are overloaded, checks priority
        if self.is_min_heap:
            return self.heap_array[parent] > self.heap_array[child]
        else:
            return self.heap_array[parent] < self.heap_array[child]

    def _swap_elements(self, index1: int, index2: int):
        if index1 < 1 or index1 > self.last_index:
            return
        if index2 < 1 or index2 > self.last_index:
            return

        item1: HeapItem = self.heap_array[index1]
        item2: HeapItem = self.heap_array[index2]
        self.heap_array[index1] = item2
        self.heap_array[index2] = item1

        self.indices[item1.value] = index2
        self.indices[item2.value] = index1

    def _propagate_up(self, index: int):
        parent: int = int(index / 2)
        while self._elements_inverted(parent, index):
            self._swap_elements(parent, index)
            index = parent
            parent = int(index / 2)

    def _propagate_down(self, index: int):
        while index <= self.last_index:
            swap: int = index
            if self._elements_inverted(swap, 2 * index):
                swap = 2 * index
            if self._elements_inverted(swap, 2 * index + 1):
                swap = 2 * index + 1

            if index != swap:
                self._swap_elements(index, swap)
                index = swap
            else:
                break

    def enqueue(self, value: Any, priority: float):
        if value in self.indices:
            self.update_priority(value, priority)
            return

        if self.last_index == self.array_size - 1:
            old_array: list[HeapItem | None] = self.heap_array
            self.heap_array = [None] * self.array_size * 2
            for i in range(self.last_index + 1):
                self.heap_array[i] = old_array[i]
            self.array_size = self.array_size * 2

        self.last_index = self.last_index + 1
        self.heap_array[self.last_index] = HeapItem(value, priority)
        self.indices[value] = self.last_index
        self._propagate_up(self.last_index)

    def dequeue(self) -> Union[None, Any]:
        if self.last_index == 0:
            return None

        result: HeapItem = self.heap_array[1]
        new_top: HeapItem = self.heap_array[self.last_index]
        self.heap_array[1] = new_top
        self.indices[new_top.value] = 1

        self.heap_array[self.last_index] = None
        self.indices.pop(result.value)
        self.last_index = self.last_index - 1

        self._propagate_down(1)
        return result.value

    def update_priority(self, value, priority: float) -> None:
        if value not in self.indices:
            return

        index: int = self.indices[value]
        old_priority: float = self.heap_array[index].priority
        self.heap_array[index].priority = priority

        if self.is_min_heap:
            if old_priority > priority:
                self._propagate_up(index)
            else:
                self._propagate_down(index)
        else:
            if old_priority > priority:
                self._propagate_down(index)
            else:
                self._propagate_up(index)

    def peak_top(self) -> Union[HeapItem, None]:
        if self.is_empty():
            return None
        return self.heap_array[1]

    def peek_top_priority(self) -> Union[float, None]:
        obj: Union[HeapItem, None] = self.peak_top()
        if obj is None:
            return None
        return obj.priority

    def peek_top_value(self):
        obj: Union[HeapItem, None] = self.peak_top()
        if obj is None:
            return None
        return obj.value
