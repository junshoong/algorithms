from sort.bubble_sort import bubble_sort
from sort.insertion_sort import insertion_sort
from sort.selection_sort import selection_sort
import random
import pytest


@pytest.mark.skip
def test_insertion_sort():
    a = [random.randrange(100) for _ in range(10000)]
    o = a[:]
    o.sort()
    assert insertion_sort(a) == o


@pytest.mark.skip
def test_bubble_sort():
    a = [random.randrange(100) for _ in range(10000)]
    o = a[:]
    o.sort()
    assert bubble_sort(a) == o


def test_selection_sort():
    a = [random.randrange(100) for _ in range(10000)]
    o = a[:]
    o.sort()
    assert selection_sort(a) == o
