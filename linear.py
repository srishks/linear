def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [3, 5, 2, 4, 9]
target = 4
index = linear_search(arr, target)
print(f"Element {target} is at index {index}" if index != -1 else f"Element {target} not found")
