"""
<초급>
[13, 7, 5, 1, 3, 2]의 배열과 10이라는 값이 주어지고 배열안에서 2개의 값이 10이 되는 두 숫자의 idx를 찾는 문제입니다. 
array에서는 sort + two pointer를 사용하여 O(n log n) + O(n) = O(n log n)의 시간복잡도를 가졌었습니다.

해시테이블의 경우 key에 요소값을, value에 인덱스를 넣어주고 배열과 함께 비교해줍니다.
배열에서 포인터를 하나씩 옮기는데 13의 경우 -3이 필요하지만 해시테이블에 값이 없기 때문에 넘어갑니다.
7의 경우 find(3)을 하면 idx 4임을 바로 알 수 있습니다.
if를 2번 돌리는 시간복잡도 -> O(n), 해시테이블을 만드는 공간복잡도 -> O(n)이 됩니다.
따라서 공간복잡도는 발생하지만 시간복잡도는 O(n log n)에서 O(n)이 됩니다.
또한 처음에 13이 10이 되는 값인 -3을 key로 갖게 하는 등도 조금 더 빠르게 풀 수 있는 optimization한 방법입니다.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    hash_table = {}

    for idx, num in enumerate(nums):
        match_num = target - num
        match_idx = hash_table.get(match_num) # 해시테이블에 예를 들면 10 - 13 = -3이 있는지 / 있으면idx 가져오기
        print('match_idx:::', match_idx)

        if match_idx is not None:
            return [idx, match_idx] 

        hash_table[num] = idx # num: idx -> 매칭이 안된 경우 키:값으로 hash_table 만들기
        print('hash_table:::', hash_table)

print(two_sum(nums=[13,7,5,1,3,2], target=10))