from sort import *
import random
import pytest


a = [random.randrange(100) for _ in range(100)]
o = a[:]
o.sort()


@pytest.mark.skip
def test_insertion_sort():
    assert insertion_sort(a) == o


@pytest.mark.skip
def test_bubble_sort():
    assert bubble_sort(a) == o


@pytest.mark.skip
def test_selection_sort():
    assert selection_sort(a) == o


@pytest.mark.skip
def test_merge_sort():
    assert merge_sort(a) == o


# @pytest.mark.skip
def test_quick_sort():
    assert quick_sort(a) == o
