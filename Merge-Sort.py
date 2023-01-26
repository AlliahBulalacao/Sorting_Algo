# Merge Sort

def mergeSort(array):
    if len(array) > 1:
        left = array[:len(array)//2]
        right = array[len(array) // 2:]

        mergeSort(left)
        mergeSort(right)