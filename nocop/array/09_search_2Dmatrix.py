""" 

"""

matrix = [[1,3,5,7], [2,8,11,12], [4,9,14,19], [6,15,25,40]]
target_num = 14

def matrix_travel(nums, target):
    row_count = len(nums) - 1
    col_count = len(nums[0])

    pivot_row_idx = row_count
    pivot_col_idx = 0

    for _ in range(row_count + col_count - 1):
        if (pivot_row_idx < 0 or pivot_col_idx < 0) or (pivot_row_idx >= row_count or pivot_col_idx >= col_count):
            return - 1

        if nums[pivot_row_idx][pivot_col_idx] == target:
            return nums[pivot_row_idx][pivot_col_idx]

        elif nums[pivot_row_idx][pivot_col_idx] < target:
            pivot_col_idx += 1
        else:
            pivot_row_idx -= 1
    
    return -1

print(matrix_travel(matrix, target_num))