def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionSort(array):
    newArr = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        newArr.append(array.pop(smallest))
    return newArr

