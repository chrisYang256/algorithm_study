"""
insertion sorting은 bubble sorting만큼 느리고 직관적인 방법입니다.
bubble sorting과 마찬가지로 time complexity는 O(n²)이며(실재 삽입되는 곳을 찾는데는 O(log n)이지만 
이후 숫자를 shift시켜주는데 필요한 시간이 O(n)이기 때문) stable한 sorting 방법입니다.

왼쪽부터 오름차순으로 정렬한다고 했을 때 왼쪽에서 오른쪽으로 이동하면서
대상이 되는 idx를 왼쪽의 숫자들과 비교하며 대상이 되는 숫자보다 작은 숫자가 나올 경우
그 뒤에 삽입해 주면서 정렬해 나가면 됩니다.
"""

nums_arr = [7, 9, 2, 1, 3]

def insertion_sort(nums):
    for point_idx in range(1, len(nums)):
        temporary = nums[point_idx]
        idx = point_idx -1

        while 0 <= idx and temporary < nums[idx]:
            print(temporary, nums[idx])
            nums[idx +1] = nums[idx]
            idx = idx -1 
        # while문 조건에 의해 큰 수를 오른쪽으로 이동(저장)시키며 왼쪽으로 이동하다가 temporary가 nums[idx]보다 큰 경우
        # nums[idx]보다 큰 temporary를 nums[idx] 뒤에 넣어 줍니다.
        # [1,2,7,9,3] -> [1,2,7,9,9] -> [1,2,7,7,9] -> [1,2,3,7,9]
        nums[idx +1] = temporary 
        print(nums[idx +1], 'end')
    return nums

print(insertion_sort(nums_arr))