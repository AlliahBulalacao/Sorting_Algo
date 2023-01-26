# Quick Sort

def quickSort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        quickSort(array, left, p - 1)
        quickSort(array, p + 1, right)

