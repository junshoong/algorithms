from sort.bubble_sort import bubble_sort
from sort.insertion_sort import insertion_sort
import random
import pytest


# @pytest.mark.skip
def test_insertion_sort():
    a = [random.randrange(100) for _ in range(10000)]
    o = a[:]
    o.sort()
    assert insertion_sort(a) == o


# @pytest.mark.skip
def test_bubble_sort():
    a = [random.randrange(100) for _ in range(10000)]
    o = a[:]
    o.sort()
    assert bubble_sort(a) == o
