# Insertion Sort

def insertionSort(array):
    for i in range(1, len(array)):

        n = array[i]
        j = i - 1

        while j >= 0 and n < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = n

    return array

array = [79, 74, 28, 90, 49, 93, 62, 72, 52, 22]
insertionSort(array)

print("Sorted array for Insertion Sort: ", array)