# Bubble Sort

def bubbleSort(array):
    index = len(array)

    for i in range(index):
        for j in (0, index - i - 1):

            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]


array = [79, 74, 28, 90, 49, 93, 62, 72, 52, 22]
bubbleSort(array)

print("Sorted array for Bubble Sort: ", array)