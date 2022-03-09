"""
<middle>
[6,3,2,5,3,-3]와 k=10가 주어졌을 때 배열 안 요소의 합이 10이 되는 subarray를 찾으면 됩니다.
hash map을 배우면 반드시 거쳐가는 문제입니다.

요소가 모두 양수라면 sliding window가 생각나야합니다.(O(n))
음수가 있는 경우 슬라이딩 위도우의 앞부분을 어디까지 진행해야 하는지 알 수 없습니다.
brute force로 이중for문을 이용해 두 개의 포인터로 서브어레이의 합을 만들 수 있습니다.(O(n³))
브루트 포스 안에 optimization하는 경우로는 첫 번째 for문 안에서 temporary sum 만들고
두 번째 for문에서 temporary sum에 값을 합해주면 됩니다.(O(n²))

이 문제는 배열과 해시맵을 이용해 두 수의 합이 sum이 되는 요소들을 찾는 two sum 문제와 비슷합니다.
이를 활용하기 위해서 subarray를 추출하는 방법을 고안해야 합니다.
cumalative sum different를 통해 할 수 있으며 cumalative sum 6,3,2,5,3에서  2,5,3를 추출하고 싶은 경우
또다른 cumalative sum 6, 3을 빼면 됩니다.
먼저 [6,3,2,5,3,-3]에 대한 cumalative sum인 [6,9,11,16,19,16]을 만듭니다.
그리고 이 cumalative sum을 hash map으로 만들어주는데 중복되는 key값이 있을 수 있으므로 value를 배열로 만들면
{6: [0], 9: [1], 11: [2], 16: [3, 5], 19: [4]}가 됩니다.
자세한 내용은 식에 풀어서 설명하겠습니다.

TC는 cumalative sum을 만들 때 필요한 O(n), hash map을 만들 때 필요한 O(n), 
각 요소의 hash map key를 찾을 때 필요한 O(n), cumalative sum에서 subarray를 추출할 때 필요한 O(n)까지 총 O(n)이 필요하고
SC cumalative sum을 만들 때 O(n), hash map을 만들 때 O(n)으로 총 O(n)이 필요합니다.
"""

from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    cumalative_sums = []
    temporary_sum = 0
    for num in nums: # 누적 합계 만들면서 넣어줌
        temporary_sum += num
        cumalative_sums.append(temporary_sum)

    table = {}
    count = 0
    # 만약 array 맨 처음부터 시작하여 누계가 k가 되는 케이스가 있다면 앞에 비교대상이 있어야 함(엣지 케이스)
    # k가 10이고 cumalative_sum - k가 0이라면 아래 식과 같은 경우 0이 table에 존재해야 하기 때문에 생성해줘야함.
    table[0] = [-1]  
    for idx, cumalative_sum in enumerate(cumalative_sums):
        # 현재 위치까지의 누계에서 k값을 뺀 값은 그 단일값 혹은 누계를 제되하면 0이 되고
        # 곧 이 값(누계) 이후부터 현재까지 누계가 k값이 되는 subarray가 됩니다.
        # 현재누계 16 - k값 10 = 6, 누계 6이 되는 idx 이후 값은 10이 되므로 k가 됨.
        target = cumalative_sum - k 
        if target in table:
            # len(table[target])이 2라면 array에 동일한 수가 2개 있다는 의미이고 해당하는 subarray가 2라는 의미
            count += len(table[target]) 

        if cumalative_sum not in table: 
            table[cumalative_sum] = [idx]
        else:
            # 누계값을 쌓아주되 -값에 의해 array에서 중첩되는 값이 생길 수 있으므로 해당 key의 value에 idx를 추가해줌
            table[cumalative_sum].append(idx) 

    print(cumalative_sums)
    print(table)
    return count

print(subarraySum(nums=[6,3,2,5,3,-3],k=10))