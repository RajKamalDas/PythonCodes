def binarySearch(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
find = 12

result = binarySearch(arr, find)
if result != -1:
    print(f"Index of {find} is {result}")
else:
    print(f"Index of {find} is not found")
