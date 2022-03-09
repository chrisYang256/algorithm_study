"""
merge sort는 O(n log n)의 시간복잡도를 가지며 stable한 알고리즘입니다.
"""

from typing import List

arr = [5,2,9,3,4,1,6]

def merge_sort(nums:List[int]) -> List[int]:
    length = len(nums)
    if length == 1:
        # print('nums:::',nums)
        return nums

    mid = length //2

    left_nums = nums[:mid]
    print('left_nums:::', left_nums)
    right_nums = nums[mid:]
    print('right_nums:::', right_nums)

    sorted_left = merge_sort(nums = left_nums) 
    print('sorted_left:::', sorted_left)
    sorted_right = merge_sort(nums = right_nums)
    print('sorted_right:::', sorted_right)

    sorted_nums = []
    idx_left = 0
    idx_right = 0
    while idx_left < len(sorted_left) or idx_right < len(sorted_right):
        print(idx_left, len(sorted_left), idx_right, len(sorted_right))
        if idx_left == len(sorted_left):
            sorted_nums.append(sorted_right[idx_right])
            print('idx_left == len(sorted_left):::', sorted_right[idx_right])
            idx_right +=1
            continue

        if idx_right == len(sorted_right):
            sorted_nums.append(sorted_left[idx_left])
            print('sorted_nums.append(sorted_left[idx_left]):::', sorted_left[idx_left])
            idx_left +=1
            continue

        if sorted_right[idx_right] <= sorted_left[idx_left]:
            sorted_nums.append(sorted_right[idx_right])
            print('sorted_right[idx_right] <= sorted_left[idx_left]:::', sorted_right[idx_right], sorted_left[idx_left])
            idx_right +=1
        else:
            sorted_nums.append(sorted_left[idx_left])
            print('else:::', sorted_right[idx_right], sorted_left[idx_left])
            idx_left +=1

    print('sorted_nums:::', sorted_nums)
    return sorted_nums

print(merge_sort(arr))