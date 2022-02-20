"""
어떤 element를 하나 선택하여 swap해주는 알고리즘으로 O(n²)를 가지며 
[[7,'a'],[7,'b'],[5,'a'],[5,'b'],[3,'c']]의 정렬 결과는 [[3, 'c'], [5, 'a'], [5, 'b'], [7, 'b'], [7, 'a']]로 stable하지 않습니다.

오름차순 정렬 기준으로 가장 왼쪽 숫자를 기준으로 하고 다음에 이어지는 숫자들중 가장 작은 수를 찾아 swap합니다. 
다음 순환 때는 그 다음 숫자를 기준으로 똑같이 반복하는 방법입니다.
"""

nums_arr = [5,9,6,3,1]

def sort_nums(nums):
    for idx in range(0, len(nums)):
        min_num = nums[idx] # 초깃값 / 가장 작은 수 저장
        min_idx = idx # 초깃값 / 가장 작은 수의 idx 저장
        for i in range(idx, len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
                min_idx = i
        print(nums[min_idx], nums[idx])
        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
        print(nums[idx], nums[min_idx])

    return nums

print(sort_nums(nums_arr))
print('-----------------')

complex_arr = [[7,'a'],[7,'b'],[5,'a'],[5,'b'],[3,'c']]

def unstable_sort(nums):
    for idx in range(0, len(nums)):
        min_num = nums[idx][0]
        min_dix = idx
        for i in range(idx, len(nums)):
            if nums[i][0] < min_num:
                min_num = nums[i][0]
                min_dix = i
        nums[idx], nums[min_dix] = nums[min_dix], nums[idx]

    return nums

print(unstable_sort(complex_arr))
