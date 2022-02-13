array = [8, 2, 1, 9, 3, 6, 2]

def find_pivot_index(values):
    total_sum = sum(values)
    left_sum = 0
    right_sum = total_sum

    past_pivot = 0
    for i in range(len(array)):
        pivot = values[i]
        right_sum = right_sum - pivot
        left_sum = left_sum + past_pivot

        if left_sum == right_sum:
            return i
        
        past_pivot = pivot
    
    return -1

print(f'The index of pivot is {find_pivot_index(array)}')