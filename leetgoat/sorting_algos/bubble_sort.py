def bubble_sort(arr):

    sorted = False
    j = 0
    while not sorted:
        sorted = True

        for i in range(1, len(arr)-j):
            if arr[i-1] > arr[i]:
                sorted = False
                arr[i-1], arr[i] = arr[i], arr[i-1]
        j += 1
    print(arr)

bubble_sort([13, 46, 24, 52, 20, 9])
