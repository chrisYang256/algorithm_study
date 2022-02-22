""" 
< sorted 2d matrix 배열에서 특정 숫자를 찾는 문제 >

문제의 경우 각 행은 좌에서 우로, 각 열은 위에서 아래로 커지는 패턴을 알 수 있습니다.
따라서 첫 행의 마지막 위치부터 탐색을 시작할 경우에
찾고자 하는 숫자가 행의 마지막 숫자보다 크다면 해당 행은 모두 탐색할 필요가 없고 다음 행으로 이동하면 됩니다.
만약 찾는 숫자가 기준점의 숫자보다 작다면 기준점 위로는 위의 과정을 거쳤거나 첫 행이므로 탐색이 필요 없고,
아래로는 기준점보다 큰 수이기 때문에 탐색이 필요 없어지므로 기준점이 위치한 열은 모두 탐색할 필요 없이
기준점보다 작은 수가 위치한 왼쪽으로 이동하면 됩니다.
"""

matrix = [
    [1,3,5,7], 
    [2,8,11,12], 
    [4,9,14,19], 
    [6,15,25,40]
]
target_num = 6

def matrix_travel(nums, target):
    row_count = len(nums[0])
    col_count = len(nums)

    pivot_row_idx = row_count - 1
    pivot_col_idx = 0

    for _ in range(row_count + col_count - 1):
        if (pivot_row_idx < 0 or pivot_col_idx < 0) or (pivot_row_idx >= row_count or pivot_col_idx >= col_count): #idx가 배열을 넘으면(찾는 숫자가 없으면) 종료
            return - 1

        if nums[pivot_row_idx][pivot_col_idx] == target:
            return [pivot_row_idx, pivot_col_idx]

        elif nums[pivot_row_idx][pivot_col_idx] < target:
            pivot_col_idx += 1

        else:
            pivot_row_idx -= 1
    
print(matrix_travel(matrix, target_num))