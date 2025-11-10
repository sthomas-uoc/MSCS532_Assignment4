
def make_heap(arr, size, idx):

    # print(f"Input: {arr} {size}, {idx}")
    
    # Assume current node index has the largest value
    largest = idx

    # The left child node index
    left = (2 * idx) + 1

    # The right child node index
    right = (2 * idx) + 2

    # Check if left child is the largest
    if left < size and arr[left] > arr[largest]:
        largest = left

    # Check if right child is the largest
    if right < size and arr[right] > arr[largest]:
        largest = right

    # If current node was not the largest, swap values
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]

        # Check recursively for the child trees
        make_heap(arr, size, largest)

    # print(f"Heaped: {arr}")

