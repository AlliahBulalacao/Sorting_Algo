# Selection Sort

def selectionSort(array, size):
    for i in range(size):
        index = i

        for j in range(i + 1, size):
            if array[j] < array[index]:
                index = j

        (array[i], array[index]) = (array[index], array[i])

array_list = [79, 74, 28, 90, 49, 93, 62, 72, 52, 22]
size = len(array_list)
selectionSort(array_list, size)


