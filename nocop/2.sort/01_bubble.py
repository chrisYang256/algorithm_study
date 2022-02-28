"""
오름차순 sorting을 예시로 배열의 0번 idx와 1번 idx를 비교 후 0번이 더 큰 경우 둘을 swap해 주고 아니면 swap하지 않습니다.
그 다음은 1번 idx와 2번 idx를 비교하는 식으로 배열의 끝 까지 반복합니다.
최초 한 번의 순회를 마쳤다면 우선 배열의 마지막은 가장 큰 수가 위치해 있게 되고 다음 순회 시에 비교할 필요가 없어집니다.
이렇게 반복하면 끝에서부터 가장 큰 수부터 정렬이 되고 마지막에 idx 0과 idx 1을 비교한 후 sorting이 종료됩니다.

time complexity는 O(n)이 필요한 동작이 총 n번 반복이 되므로 O(n²)이 되며 bubble sorting은 평균적으로 O(n²)을 가지기 때문에 속도가 느립니다.
또다른 bubble sorting 특징으로는 stable solting이라는 점입니다.
[[7,'a'], [7,'b'], [5,'a'], [5,'b'], [3,'c']]를 bubble sorting하면 [[3, 'c'], [5, 'a'], [5, 'b'], [7, 'a'], [7, 'b']]와 같이 stability하게 정렬됩니다.
qick sorting의 경우 stable하지 않게 정렬됩니다.
"""

from typing import List


nums_arr = [7, 9, 2, 1, 3]

def sort(nums: List[int]) -> List[int]:
    for idx in range(0, len(nums) -1):
        for i in range(0, len(nums) -idx -1):
            if nums[i] > nums[i +1]:
                nums[i], nums[i +1] = nums[i +1], nums[i]
    return nums

print(sort(nums_arr))
print('------------------')

complex_arr = [[7,'a'], [7,'b'], [5,'a'], [5,'b'], [3,'c']]

def stable_sort(arr):
    for idx in range(0, len(arr) -1):
        for i in range(0, len(arr) -idx -1):
            if arr[i][0] > arr[i +1][0]:
                arr[i], arr[i +1] = arr[i +1], arr[i]
    
    return arr

print(stable_sort(complex_arr))