"""
<middle>
1,3,5,7,9라는 리스트가 있고 이 리스트는 다음을 가리키는 next뿐만 아니라 random한 노드를 지정하는 ramdom포인터까지
각 노드가 지니고 있습니다.
이 랜덤 포인트까지 deep copy하는 문제입니다.

우선 원본리스트에 current read포인터를 두고 새 리스트에는 더미노드를 넣고 current write포인터를 지정한 후
더미노드 이후로 하나씩 연결하면서 랜덤포인트를 제외한 기본 노드를 카피합니다.
문제가 어려운 이유는 새로운리스트가 원본리스트의 random포인트를 가리키는게 아닌 새로운리스트 안에 있는 노드를
가리켜야하고 또한 원본리스트의 노드가 새로운리스트의 노드를 가리키는 정보도 없기 때문입니다.
하지만 바로 이 부분이 힌트가 됩니다.
각각의 노드는 포인트이면서 레퍼런스이기 때문에 각각의 노드 정보가 다른 데이터스트럭쳐에 들어갈 수 있습니다.
이것을 이용하여 hash map을 통해 원본리스트와 새로운리스트를 연결할 수 있습니다.
key에는 원본리스트의 포인터/레퍼런스를, value에는 새로운리스트의 포인터/레퍼런스로 지정해주면 됩니다.
이후 key를 참조해 원본리스트의 랜덤포인터의 정보를 알아내어 새로운리스트에서 참고하여 연결시켜주면 됩니다.
TC는 리스트를 전부 순회하는데 필요한 O(n), SC는 hash map을 만드는데 필요한 O(n)이 됩니다.

hash map 없이 TC O(n), SC O(1)로 풀이하는 법:
카피하면서 원본 링크드리스트의 노드가 복사된 노드를 가리키게 하고
복사된 노드는 원본노드의 다음번 노드를 가리키게 하면서 서로 지그재그 모양으로 링크시켜줍니다.
1  3   5  7   9   x
| / \ / \/ \ / \ /
1    3   5  7   9
죄송합니다 그리그리기가 귀찮아서.
이제 원본노드를 읽어 random포인터의 정보를 가져왔을 때 만약 원본노드 1의 random포인터가 5를 가리킨다면 
원본노드 5는 복사 노드의 5를 가리키기 때문에 복사 노드1의 random포인터를 5로 지정하면 됩니다.
이 동작을 원본노드를 순차적으로 돌며 반복하면 자연스레 복사노드의 random포인터도 동일하게 지정됩니다.
이후 다시 원본노드의 처음으로 돌아와 원본노드의 next가 가리키는 복사노드가 가리키는 노드를 
원본노드에게 재연결하고 복사노드 역시 같은 방식으로 연결을 업데이트하면서 원래의 링크의 순서대로 next를 바꾸면 됩니다.
"""

import random
from typing import List
from unittest import runner


class RandomListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def create_list(list: List[int]) -> RandomListNode:
    if len(list) == 0:
        raise RuntimeError('no elem')

    head_node = RandomListNode(list[0])
    last_node = head_node
    for idx in range(1, len(list)):
        node = RandomListNode(list[idx])
        last_node.next = node
        last_node = node
    return head_node

def print_nodes(head: RandomListNode):
    cur_node = head
    while cur_node:
        print(cur_node.val, end=' ')
        random_node = cur_node.random
        if random_node: # 랜덤 노드가 노드프린트로 들어오는 경우
            print(random_node.val, end=' ')
        else:
            print(random_node, end=' ')
        cur_node = cur_node.next
    print()

def add_random(head: RandomListNode):
    node_array = []
    cur_node = head
    while cur_node:
        node_array.append(cur_node)
        cur_node = cur_node.next
    node_count = len(node_array)
    cur_node = head
    while cur_node:
        random_idx = random.randint(0, node_count - 1) # 노드 한 개는 다음이 없어야하므로 총 노드 갯수에서 - 1 
        cur_node.random = node_array[random_idx]
        cur_node = cur_node.next

class RandomDeepCopy:
    def hash_way(self, head: 'Node') -> 'Node':
        dummy_node = RandomListNode(-1)

        node_map = {}

        cur_read_node = head
        cur_write_node = dummy_node
        while cur_read_node: # 랜덤포인트 제외 복사 / 해시맵에 매칭
            val = cur_read_node.val
            temp_node = RandomListNode(val)

            node_map[cur_read_node] = temp_node
            cur_write_node.next = temp_node # hash map의 vlaue와 '메모리 주소'가 이어진다고 보면 됨
            cur_read_node = cur_read_node.next
            cur_write_node = cur_write_node.next

        cur_read_node = head
        while cur_read_node:
            from_node = node_map[cur_read_node] # value 가져오기(원본과 링크된 복사한 값)
            random_node = cur_read_node.random # 원본에서 랜덤노드 뽑기
            if random_node is not None:
                to_node = node_map[random_node] # 랜덤노드를 찾아서 
                from_node.random = to_node # vlaue에 랜덤노드 복사
            else:
                from_node.random = None
            cur_read_node = cur_read_node.next

        return dummy_node.next

    def node_match(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        cur_node = head
        while cur_node: # 복사노드 생성 / 원본노드와 복사노드 지그재그 연결작업
            val = cur_node.val
            temp_node = RandomListNode(val) # 원본.val 복사한 임시노드 생성
            temp_node.next = cur_node.next # 임시노드의 연결노드를 원본노드의 다음노드와 연결 
            cur_node.next = temp_node # 원본노드의 다음 노드를 임시노드에 연결로 업데이트
            cur_node = cur_node.next
        
        cur_node = head
        while cur_node: # 랜텀 포인터 복사
            from_node = cur_node.next # 위에서 원본노드와 복사노드를 교차 지정했기 때문에 복사노드를 가리킨다고 보면 됨
            to_node = None
            if cur_node.random:
                to_node = cur_node.random.next # 교차연결 덕분에 원본노드의 랜덤포인터의 next는 복사한 노드의 노드가 됨

            from_node.random = to_node # 원본노드를 통해 찾은 random포인터를 복사노드의 랜덤포인트로 복사해줌
            cur_node = cur_node.next.next # 교차연결 때문에 원본.next.next는 사실상 원래 원본리스트에서 원본.next와 같음

        cur_node = head
        dummy_node = RandomListNode(-1)
        dummy_node.next = cur_node.next # 원본노드.next는 복사노드의 첫번째 노드

        while cur_node and cur_node.next: # 지그재그된 노드 재정렬, 원본노드의.next인 복사노드가 없으며 끝
            temp_node = cur_node.next 
            cur_node.next = cur_node.next.next # cur_node.next -> 복사노드의 같은값, cur_node.next.next는 원래 원본리스트의 현재노드의 다음값
            cur_node = temp_node

        return dummy_node.next

list1 = create_list([1,3,5,7,9])

add_random(list1)
print_nodes(list1)

random_deep_copy = RandomDeepCopy()

deep_copy = random_deep_copy.hash_way(list1)
print_nodes(deep_copy)