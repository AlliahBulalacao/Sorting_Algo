def bubbleSort(array):
    index = len(array)

    for i in range(index):
        for j in (0, index - i - 1):

            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]


