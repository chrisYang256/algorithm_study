"""
<middle>
[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1)]이라는 좌표가 주어지고 이를 통해 만들어지는 직사각형 중
가장 작은 직사각형의 사이즈를 구하는 문제입니다.
.  .  .
.  .  .
.  .  .  .
해당 좌표를 점으로 표현하면 이와같은 모양이 됩니다.(예시에 없는 (0,0) 등은 제외)
사각형은 왼쪽 아래, 오른쪽 위 쌍이나 왼쪽 위, 오른쪽 아래의 쌍의 좌표가 주어지면 다른 나머지 좌표를 찾아낼 수만 있다면 사각형이 됩니다.
.  .  *
.  .  .
*  .  .  .
(x,y)좌표값이라 생각하고 (1,1), (3,2)가 주어진다면 
(1,1)의 첫번째가 x값, (3,2)의 두번째가 y값이 되어 (1,2)가
그리고 (3,2)의 첫번째가 x값, (1,1)의 두번째가 y값이 되어 (3,1)이 됩니다.

for문을 통해 해결하려면 처음 for문에서 각각의 포인트 (1,1), (3,2)를 찾고
두번째 for문에서 이 쌍에 맞는 x,y값을 구합니다.
그리고 세 번째 for문에서 (1,2), (3,1)인 값을 배열에서 찾으면 O(n³)이 됩니다.
여기서 세번째 for문은 data structure를 통해 O(1)로 만들 수 있고 hash를 이용하면 됩니다.
hash map of hash set을 이용할 수 있습니다.(x,y 포인트가 어떤 값을 가질 필요가 없기 때문에 hash map of hash map일 필요는 없습니다.)
hash set은 {1: {1, 2, 3}}가 있는 경우 {1, 2, 3}을 set이라고 합니다.
두번째 for문에서 hash map of hash set인 {1: {1, 2, 3}, 2: {1, 2, 3}, 3: {1}}를 만들면 
(1,2), (3,1)을 key를 찾는데 O(1), value를 찾는데 O(1)로 구할 수 있습니다.

TC는 이중for문과 해당 포인트를 hash map에서 찾는 시간 O(n²), 총 n개의 점들을 hash map of hash set에 저장하는 O(n)이 됩니다.
hashset을 dynamic array or linked-list로 하는 경우 find time complexity O(1)이 , O(n)으로 바뀌기 때문에 크게 느려집니다.
"""

from typing import List  
import sys

def min_ract(points: List[List[int]]) -> int:
    table = {}
    for point in points:
        x = point[0]
        y = point[1]
        if x not in table:
            table[x] = set() # hash set
        table[x].add(y)
    min_area = sys.maxsize
  
    for first_idx in range(len(points)): # 예: 왼쪽 아래 좌표
        first_point = points[first_idx]
        point_x0 = first_point[0]
        point_y0 = first_point[1]
        for second_idx in range(first_idx+1, len(points)): # 예: 오른쪽 위 좌표
            second_pt = points[second_idx]
            point_x1 = second_pt[0]
            point_y1 = second_pt[1]
        
            # (1,1), (3,2) -> (1 - 3) * (1 - 2) -> 2 * 1 -> 2
            # 만약 (1,3), (1,3)인 경우 0이 되는데 즉, 같은 값이 들어오면 좌표 두개가 한 점이기 때문에 pass
            # 혹은 (1,3), (1,2)나 (2,4), (1,4)의 경우는 두 좌표가 한쪽에 쏠려있는 형태로 둘 중 하나는 0 즉 x*0 or 0*x = 0이고
            # 형태적으로 두 점이 대각선상에 있지 않기 때문에 직사각형을 구할 수 없어 pass
            expected_area = abs(point_x0 - point_x1) * abs(point_y0 - point_y1)
            if expected_area == 0:
                continue
            
            point2 = (point_x0, point_y1) # (1,1), (3,2) -> (1,2)
            point3 = (point_x1, point_y0) # (1,1), (3,2) -> (3,1)
            
            set2 = table[point2[0]] # table에서 x값인 key찾아 hash set을 불러옴
            if point2[1] not in set2: # hash set 안에 y값인 value가 없다면 사각형이 되는 좌표값이 없는것
                continue
                
            set3 = table[point3[0]]
            if point3[1] not in set3:
                continue
            
            print(min_area, expected_area)
            min_area = min(min_area, expected_area)
    
    if min_area == sys.maxsize:
        min_area = 0

    print(table) 
    return min_area

print(min_ract(points=[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1)]))