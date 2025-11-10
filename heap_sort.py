
from heap_ds import make_heap

def heap_sort(inp):

    size = len(inp)

    # Make heap
    for i in range(size // 2 - 1, -1, -1):
        make_heap(inp, size, i)

    # Extract elements
    for i in range(size - 1, 0, -1):
        # Move the largest to the end of the heap array
        inp[i], inp[0] = inp[0], inp[i]
        # Remake the heap but only till the previously marked largest ones
        make_heap(inp, i, 0)

    # Return the input to match the test function expectations
    return inp

