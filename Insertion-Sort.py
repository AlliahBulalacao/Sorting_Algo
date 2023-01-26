# Insertion Sort

def insertionSort(array):
    for i in range(1, len(array)):

        n = array[i]
        j = i -1

        while j >= 0 and n < array[j]:
            array[j + 1] = array[j]
            j -= 1

    return array