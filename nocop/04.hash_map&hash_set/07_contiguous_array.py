"""
<middle>
[1,0,1,1,1,0,0,1,1]라는 배열이 주어졌을 때 1의 갯수와 0의 갯수가 같은 최대길이의 subarray를 찾는 문제입니다.
1은 그대로 가져오고 0은 -1로 바꿔서 합이 0이 되는 경우를 찾으면 문제에서 찾고자하는 subarray가 된다는 것을 알 수 있습니다.
만약 배열이 [b,a,b,b,b,a,a,b,b]일 경우 b를 1로 바꾸고 a를 -1로 바꾸기만 하면 같은 맥락으로 풀이할 수 있습니다.
이 패턴대로 누계를 하면 [1, 0, 1, 2, 3, 2, 1, 2, 3]가 되는데 앞에서부터 첫 1이 다시 1을 만났을 때 처음 1을 뺀 나머지 길이를
원래의 배열에서 보면 0, 1로 같은 갯수를 갖게됩니다.
첫 1이 다음 1을 만나게 되는 경우를 보면 [1,0,1,1,1,0,0]로 다시 자신을 제외하는 경우 [0,1,1,1,0,0]으로 0과 1의 갯수가 같으며
길이는 6이 됩니다.
가장 빠르게 탐색할 수 있는 방법으로 각 누계를 {0: [1], 1: [0, 2, 6], 2: [3, 5, 7], 3: [4, 8]}과 같이 hash table에 idx와 함께 넣고
계산하여 그 길이를 재는 방법이 있습니다.
누계 1의 idx 6에서 idx 0을 빼면 6이 되는데 이는 원본 배열에서 [0,1,1,1,0,0]을 가리키며 길이는 6이 됩니다.
여기서 주의할 점은 위와 같은 경우 누계에 0은 존재하고 길이는 2가 되어야 합니다.
하지만 비교군이 없기 때문에 해시 table에 0 = [-1]이라는 edge case를 미리 만들어줘여합니다.
그럼 {0: [-1, 1], 1: [0, 2, 6], 2: [3, 5, 7], 3: [4, 8]}와 같은 table이 되고
1 - (-1) = 2이므로 원본배열 [1,0]의 길이인 2와 일치하게 됩니다.
"""

from typing import List

def contiguous_arr(nums: List) -> int:
    cumalative_sums = []
    temporary_sum = 0

    for num in nums:
        if num == 0:
            num = -1
        
        temporary_sum += num
        cumalative_sums.append(temporary_sum)
    print(cumalative_sums)

    table = {}
    table[0] = [-1]
    max_length = 0
    for idx, sum in enumerate(cumalative_sums):
        if sum in table:
            table[sum].append(idx)
        else:
            table[sum] = [idx]
        print(table)

        indices = table[sum]
        length = indices[-1] - indices[0] # 가장 끝 누계에서 첫 누계를 뺀 수가 그 hash key의 가장 긴 subarray의 길이가 됨
        max_length = max(length, max_length)
    return max_length

print(contiguous_arr(nums=[1,0,1,1,1,0,0,1,1]))