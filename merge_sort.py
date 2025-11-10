
def merge_sort(inp):
    
    inp_len = len(inp)

    # Input length will be 1 when the conquer has reached the single element
    if inp_len <= 1:
        return inp

    split = inp_len // 2

    # Divide
    left = inp[:split]
    right = inp[split:]

    # Conquer
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Combine
    merged = merge(sorted_left, sorted_right)
    
    return merged

def merge(left, right):

    sorted = []
    i = 0
    j = 0

    # Compare the two arrays and add the lower value to the sorted array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i +=1
        else:
            sorted.append(right[j])
            j += 1

    # add any remaining values
    while i < len(left):
        sorted.append(left[i])
        i += 1
    while j < len(right):
        sorted.append(right[j])
        j += 1

    return sorted
