def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        p = i
        while p > 0 and arr[p-1] > val:
            arr[p] = arr[p-1]
            p -= 1
        arr[p] = val
    return arr
