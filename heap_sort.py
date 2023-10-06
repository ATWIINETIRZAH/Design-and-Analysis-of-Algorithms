def heapify(array, n, i):
    largest = i  # Initialize the largest as the root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If the left child is larger than the root
    if left < n and array[left] > array[largest]:
        largest = left

    # If the right child is larger than the largest so far
    if right < n and array[right] > array[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # Swap the two
        heapify(array, n, largest)

def heap_sort(array2):
    n = len(array2)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array2, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        array2[i], array2[0] = array2[0], array2[i]  # Swap
        heapify(array2, i, 0)

# Example usage:
test_list = [4, 6, 8, 10, 1, 4, 9]
heap_sort(test_list)
print(test_list)  # Output will be the sorted list
