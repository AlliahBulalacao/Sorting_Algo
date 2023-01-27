# Merge Sort

def mergeSort(array):
    if len(array) > 1:
        left = array[:len(array)//2]
        right = array[len(array) // 2:]

        mergeSort(left)
        mergeSort(right)

        i = 0 #left_index
        j = 0 #right_index
        k = 0 #merge_index

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array = right[j]
                j += 1
                k += 1

