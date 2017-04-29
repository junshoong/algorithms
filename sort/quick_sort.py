def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)-1
    if start < end:
        p = _partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)

    return arr


def _partition(arr, start, end):
    left = start
    for p in range(start, end):
        if arr[p] < arr[end]:
            arr[p], arr[left] = arr[left], arr[p]
            left += 1
    arr[left], arr[end] = arr[end], arr[left]
    return left
