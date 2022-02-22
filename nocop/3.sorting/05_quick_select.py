"""
배열에서 n번째로 큰 수를 찾는 문제입니다.

- solution1: 
배열을 오름차순으로 정렬하고 뒤에서 두번째 숫자를 선택할 경우 time complexity는 O(n log n)입니다.

- solution2:
heap을 이용하는 경우 time complexity는 O(n log K)입니다.

- solution3:
partitioning을 적용합니다.
pivot을 설정하고 피봇보다 작은 그룹과 큰 그룹으로 파티셔닝 하는 방식입니다.
세가지 솔루션 중에 가장 빠릅니다.
"""

import random


arr = [5,7,9,3,1,2,4]
n = 7

# partitioning
def quick_select(nums, nth):
    length = len(nums)
    if length == 1:
        return nums[0]

    pivot_idx = random.randrange(length)
    last_idx = length - 1

    nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx] # 피봇을 끝으로 보내줌
    left_idx = 0           
    right_idx = length - 2 
    pivot = nums[-1]
    while left_idx <= right_idx: 
        if nums[left_idx] <= pivot: # left 포인터의 왼쪽은 피봇과 같거나 작은 수가 위치하도록
            left_idx += 1
            continue

        if pivot < nums[right_idx]: # right 포인터의 오른쪽은 피봇보다 큰 수가 위치하도록
            right_idx -= 1
            continue
        
        if nums[left_idx] > pivot and pivot > nums[right_idx]: # 둘 다 멈춘 경우 두 숫자를 swap하여 진행을 계속함
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
            continue
    
    # left_idx는 결국 가장 큰 수에서 멈춤
    # nums[left_idx]과 nums[last_idx](즉, pivot)를 교체하면 결국 pivot의 왼쪽으로는 pivot보다 작은 수들이, 오른쪽에는 큰 수들이 있게됨
    # pivot은 자신이 있어야할 순서에 위치하게 됨
    nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx] 

    # 배열은 pivot을 기준으로 계속해서 pivot보다 큰수들과 작은수들의 묶음으로 나뉘고 length - nth이 속한 쪽을 찾아감
    # 배열이 (오름차순으로)정렬되면서 length - nth의 값은 곧 nth번째의 값을 가리키는 idx가 되는데
    # 이 length - nth의 값과 left_idx가 일치하는 경우 nth번째의 값을 찾았다고 판단하며 아래와 같이 재귀를 통해 탐색해 나감
    if left_idx == length - nth:
        return nums[left_idx]

    elif left_idx < length - nth:
        print('nums[left_idx+1:]:::', nums[left_idx + 1:])
        return quick_select(nums=nums[left_idx + 1:], nth=nth) # pivot은 이미 자신의 자리를 찾았기 때문에 제외

    elif length - nth < left_idx:
        return quick_select(nums=nums[:left_idx], nth=nth - (length - left_idx)) # pivot은 이미 자신의 자리를 찾았기 때문에 제외

print(quick_select(arr, n))