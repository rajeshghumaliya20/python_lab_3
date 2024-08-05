def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Pass {i}: {arr}")
elements = [1, 4, 2, 8, 23]
print("Initial array:", elements)
insertion_sort(elements)
print("Sorted array:", elements)