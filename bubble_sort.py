def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(array)-1):
            if array[i]>array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
    return array