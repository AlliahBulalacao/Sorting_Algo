# Quick Sort

def quickSort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        quickSort(array, left, p - 1)
        quickSort(array, p + 1, right)

def partition(array, left, right):
    g = left
    h = right - 1
    pivot = array(right)

    while g < h:
        while g < right and array[g] < pivot:
            g += 1
        while h > left and array[h] >= pivot:
            h -= 1

        if g < h:
            array[g], array[h] = array[h], array[g]

    if array[g] > pivot:
        array[g], array[right] = array[right], array[g]

    return g

