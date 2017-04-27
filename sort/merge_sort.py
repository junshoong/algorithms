def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    size = len(arr)//2
    right = merge_sort(arr[:size])
    left = merge_sort(arr[size:])

    return _merge(left, right)


def _merge(left, right):
    arr = []
    l_p, r_p = 0, 0
    while l_p < len(left) and r_p < len(right):
        if left[l_p] <= right[r_p]:
            arr.append(left[l_p])
            l_p += 1
        else:
            arr.append(right[r_p])
            r_p += 1

    if left:
        arr += left[l_p:]
    if right:
        arr += right[r_p:]

    return arr
