"""
<middle>
[1,1,1,1,3,3,3,5,5,2,2,4,6], k=2라는 배열과 숫자가 주어졌을 때
배열에서 가장 많은 순서대로 k개의 요소를 리턴하는 문제입니다.

solution1:
해시맵에 키에는 요소를, 값에는 빈도수를 넣어줍니다.
그리고 이 값을 배열 [(키,값), (키,값), (키,값)]과 같이 만들고 값을 기준으로 정렬 후 k만큼 키를 리턴합니다.

solution2:
해시맵에 키에는 요소를, 값에는 빈도수를 넣어줍니다.
그리고 배열에 [키, 키, 키]만 넣어주고 해시맵을 통해 비교하며 정렬 후 k만큼 리턴합니다.
해시맵을 만드는 TC O(n), 배열을 정렬하는 TC O(n log n)이 되고 O(n log n)이 됩니다. SC는 O(n)입니다.

기타:
O(n log k)를 만들려면 heap을 만들어 해결할 수 있습니다(k는 k=2를 말합니다.)
"""

from typing import List

def freq(nums: List, k: int) -> List:
    table = {}

    for e in nums:
        is_there = table.get(e)
        if is_there is None:
            table[e] = 1
        table[e] +=1

    keys = []
    for e in table.items():
        keys.append(e)
    print('t',table)
    print(keys)

    sort = sorted(keys, key=lambda key: key[1], reverse=True)

    result = []
    for i in range(k):
        result.append(sort[i][0])

    return result 

print(freq(nums=[1,1,1,1,3,3,3,5,5,2,2,4,6], k=3))

print('----------')

# 강사님 heapq 사용 솔루션
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    table = {}    
    for num in nums:
      count = table.get(num)
      if count is None:
        table[num] = 0      
      table[num] += 1
           
    #heap 
    freq_heap = []
    for num, count in table.items():
      heapq.heappush(freq_heap,(count, num))
      if k < len(freq_heap):
        heapq.heappop(freq_heap)
    
    k_freq = []
    while freq_heap:
      count , num = freq_heap[0]
      heapq.heappop(freq_heap)
      k_freq.append(num)
    k_freq.reverse()
    
    return k_freq

print(topKFrequent(nums=[1,1,1,1,3,3,3,5,5,2,2,4,6], k=2))