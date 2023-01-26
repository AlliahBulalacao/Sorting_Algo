# Quick Sort

def quickSort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        quickSort(array, left, p - 1)
        quickSort(array, p + 1, right)

def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    return i

array = [79, 74, 28, 90, 49, 93, 62, 72, 52, 22]
quickSort(array, 0, len(array) - 1)

print("Sorted array for Quick Sort: ", array)