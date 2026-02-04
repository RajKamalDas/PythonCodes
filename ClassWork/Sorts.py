import random

elements = [11, 5, 9, 0, 3, 6]


def bubbleSort(arr):
    changes = True
    while changes:
        changes = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changes = True
    return arr


def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


random.shuffle(elements)
print(elements, end="->")
elements = bubbleSort(elements)
print(elements)

random.shuffle(elements)
print(elements, end="->")
elements = selectionSort(elements)
print(elements)

random.shuffle(elements)
print(elements, end="->")
elements = insertionSort(elements)
print(elements)

random.shuffle(elements)
print(elements, end="->")
elements = mergeSort(elements)
print(elements)
