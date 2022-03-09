"""
pivot을 기준으로 왼쪽에는 pivot보다 작은 수들을, 오른쪽에는 pivot보다 큰 수들을 위치시키는 partitioning을 사용합니다.
정렬 결과는 stable하지 않습니다.
worst case는 pivot이 계속해서 n -1, n -2처럼 순차적으로 되는 경우로 O(n)이 필요한 Partitioning procedure가 총 n번 필요하므로 O(n²)이 됩니다.
Partitioning을 계속하면 새로 잡는 pivot의 원래 위치를 알아가게 되고 모든 요소가 정렬이되게 됩니다.
best case는 pivot이 중간 값을 잡는 경우처럼 각각의 subarray들이 절반 값으로 나뉘어지고 O(n)이 log n만큼 필요하므로 O(n log n)이 됩니다.
"""

import random


arr = [5,7,9,3,1,5,5,2,4]

def quick_sort(nums, begin_idx, last_idx): 
    length = last_idx-begin_idx+1 # 8 - 1

    if length <= 1:
        return nums

    pivot_idx = random.randrange(begin_idx, last_idx+1)
    nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]
    left_idx = begin_idx
    right_idx = last_idx-1
    pivot = nums[last_idx]
    while left_idx <= right_idx:
        if nums[left_idx] <= pivot: # pivot보다 작은 수들을 왼쪽에 정렬
            left_idx += 1
            continue

        if nums[right_idx] > pivot: # pivot보다 큰 수들을 오른쪽에 정렬
            right_idx -= 1
            continue

        if nums[left_idx] > pivot and pivot >= nums[right_idx]: # 왼쪽과 오른쪽이 모두 움직일 수 없게 되면 서로 swap하고 계속 진행
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
            continue
    # 바로 위에서 swap이 끝나면 다음 반복문에서 left_idx와 right_idx는 각각 한칸씩 우, 좌로 이동함에 따라
    # 종국에 left_idx는 오른쪽에 정렬된 pivot보다 큰 숫자들 중 첫 idx를 가리키게 됨
    # while문이 끝나고 pivot값(nums[last_idx])은 정렬된 자신의 위치(좌측은 자신보다 작고 우측은 크므로)로 이동
    nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]

    # print('nums-0:::', nums)
    quick_sort(nums=nums, begin_idx=left_idx+1, last_idx=last_idx) # 자기 자리를 찾은 pivot(left_idx)의 오른쪽을 재귀로 정렬
    print('nums-1:::', nums)
    quick_sort(nums=nums, begin_idx=begin_idx, last_idx=last_idx-1) # 자기 자리를 찾은 pivot(left_idx)의 왼쪽을 재귀로 정렬
    print('nums-2:::', nums)

    return nums

quick_sort(nums=arr, begin_idx=0, last_idx=len(arr)-1)
print(arr)