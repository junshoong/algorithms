from sort import *
import random
import pytest


a = [random.randrange(10) for _ in range(1000)]
o = a[:]
o.sort()
b = [1, 1, 1, 1, 0]
o2 = [0, 1, 1, 1, 1]
c = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0]
o3 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


# @pytest.mark.skip
def test_insertion_sort():
    assert insertion_sort(a) == o
    assert insertion_sort(b) == o2
    assert insertion_sort(c) == o3


# @pytest.mark.skip
def test_bubble_sort():
    assert bubble_sort(a) == o
    assert bubble_sort(b) == o2
    assert bubble_sort(c) == o3


# @pytest.mark.skip
def test_selection_sort():
    assert selection_sort(a) == o
    assert selection_sort(b) == o2
    assert selection_sort(c) == o3


# @pytest.mark.skip
def test_merge_sort():
    assert merge_sort(a) == o
    assert merge_sort(b) == o2
    assert merge_sort(c) == o3


# @pytest.mark.skip
def test_quick_sort():
    assert quick_sort(a) == o
    assert quick_sort(b) == o2
    assert quick_sort(c) == o3
