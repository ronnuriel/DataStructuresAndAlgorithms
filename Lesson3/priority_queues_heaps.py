# -*- coding: utf-8 -*-
"""
priority_queues_heaps.py — מימוש Min-Binary-Heap ידידותי ללמידה
כולל: insert / find_min / delete_min / decrease_key / build_heap / heapsort + בדיקות קטנות.

הרצה:
    python priority_queues_heaps.py
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, Optional
import random

class MinBinaryHeap:
    """
    ערימה בינארית (מינימום) עם תמיכה ב-decrease_key בעזרת מיפוי item->index.
    נדרשת ייחודיות פר- item. אם יש כפילויות, עטפו בערכי uid.
    """
    __slots__ = ("_a", "_pos")
    def __init__(self):
        self._a: List[Tuple[int, Any]] = []   # (key, item)
        self._pos: Dict[Any, int] = {}        # item -> index

    # ---------- עזר ----------
    def _swap(self, i: int, j: int) -> None:
        self._a[i], self._a[j] = self._a[j], self._a[i]
        # עדכון מיקומים במפה
        self._pos[self._a[i][1]] = i
        self._pos[self._a[j][1]] = j

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = (i - 1) // 2
            if self._a[i][0] < self._a[p][0]:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._a)
        while True:
            l = 2*i + 1
            r = 2*i + 2
            smallest = i
            if l < n and self._a[l][0] < self._a[smallest][0]:
                smallest = l
            if r < n and self._a[r][0] < self._a[smallest][0]:
                smallest = r
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    # ---------- פעולות PQ ----------
    def insert(self, item: Any, key: int) -> None:
        if item in self._pos:
            raise ValueError("item already in heap; use decrease_key if needed")
        self._a.append((key, item))
        i = len(self._a) - 1
        self._pos[item] = i
        self._sift_up(i)

    def find_min(self) -> Tuple[int, Any]:
        if not self._a:
            raise IndexError("find_min from empty heap")
        return self._a[0]

    def delete_min(self) -> Tuple[int, Any]:
        if not self._a:
            raise IndexError("delete_min from empty heap")
        root_key, root_item = self._a[0]
        last = self._a.pop()
        del self._pos[root_item]
        if self._a:
            self._a[0] = last
            self._pos[last[1]] = 0
            self._sift_down(0)
        return (root_key, root_item)

    def decrease_key(self, item: Any, new_key: int) -> None:
        if item not in self._pos:
            raise KeyError("item not found in heap")
        i = self._pos[item]
        old_key, it = self._a[i]
        if new_key > old_key:
            raise ValueError("new_key must be <= old_key")
        self._a[i] = (new_key, it)
        self._sift_up(i)

    # ---------- build-heap ----------
    def build_heap(self, pairs: List[Tuple[int, Any]]) -> None:
        """ O(n): ממלאים מערך ומחלחלים מטה מכל אינדקס פנימי. """
        self._a = list(pairs)
        self._pos = {it: idx for idx, (k, it) in enumerate(self._a)}
        n = len(self._a)
        for i in range(n//2 - 1, -1, -1):
            self._sift_down(i)

    # ---------- עזרי בדיקה/הדגמה ----------
    def _is_heap(self) -> bool:
        n = len(self._a)
        for i in range(n):
            l = 2*i + 1
            r = 2*i + 2
            if l < n and self._a[i][0] > self._a[l][0]:
                return False
            if r < n and self._a[i][0] > self._a[r][0]:
                return False
        return True

    def __len__(self) -> int:
        return len(self._a)

    def __repr__(self) -> str:
        return f"MinBinaryHeap({self._a})"

# -------- Heapsort (עולה) בעזרת Min-Heap --------
def heapsort(iterable):
    h = MinBinaryHeap()
    # נעטוף עם uid כדי לאפשר כפילויות בערכים
    for uid, x in enumerate(iterable):
        h.insert((uid, x), x)
    out = []
    while len(h) > 0:
        k, (uid, v) = h.delete_min()
        out.append(v)
    return out

# -------- בדיקות קטנות בעת הרצה ישירה --------
def _demo():
    print("== Build-Heap O(n) + פעולות ==")
    pairs = [(5,'a'), (3,'b'), (9,'c'), (7,'d'), (1,'e'), (4,'f')]
    h = MinBinaryHeap(); h.build_heap(pairs)
    print("heap:", h)
    assert h._is_heap()

    print("min:", h.find_min())
    print("delete_min:", h.delete_min())
    print("after delete:", h)
    h.decrease_key('c', 0)
    print("after decrease_key(c->0):", h)
    assert h._is_heap()

    print("== Heapsort ==")
    arr = [7,1,9,4,2,6,3,5,8,0,7,7]
    print("in: ", arr)
    print("out:", heapsort(arr))
    print("OK.")

if __name__ == "__main__":
    _demo()
