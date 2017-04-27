def selection_sort(arr):
    for i in range(len(arr)-1):
        val, p = arr[i], i
        for j in range(i, len(arr)):
            if val > arr[j]:
                val = arr[j]
                p = j
        arr[i], arr[p] = arr[p], arr[i]

    return arr
