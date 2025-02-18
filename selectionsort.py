def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Pass {i + 1}: {arr}")
elements = [22, 13, 4, 8, 17, 26, 53, 4]
print("Initial array:", elements)
selection_sort(elements)
print("Sorted array:", elements)