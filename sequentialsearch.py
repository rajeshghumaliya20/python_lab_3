def sequential_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index 
    return -1 
elements = [1, 3, 5, 8, 10, 23, 35]
search_value = 10
result = sequential_search(elements, search_value)
if result != -1:
    print(f"Element {search_value} found at index {result}.")
else:
    print(f"Element {search_value} not found in the list.")