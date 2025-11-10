
def quick_sort(inp):

    if len(inp) <= 1:
        return inp

    # Divide using a pivot
    # Need to find a good pivot for performanc. We will use the middle value for now
    pivot = inp[len(inp) // 2]

    left = []
    middle = []
    right = []

    for a in inp:
        if a < pivot:
            left.append(a)
        elif a == pivot:
            middle.append(a)
        else:
            right.append(a)

    # Conquer by repeatedly performing the sort
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # Combine
    # Just merge the arrays as the values have the sorted
    
    return sorted_left + middle + sorted_right


