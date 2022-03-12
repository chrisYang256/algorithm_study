"""
<basic>
1,3,5,7,9와 2,7,9 라는 링크드리스트가 주어지면 교차점인 7을 리턴하는 문제입니다.

TC O(n), SC O(n):
current 포인터를 만들고 하나의 링크드리스트를 순회하며(TC O(n)) 노드들의 address들을 해시셋에 저장(SC O(n))하고 
다시 current 포인터를 다음 노드를 순회(TC O(n)하게 하면서 해시셋과 비교하며 교차점(공통된 값)을 찾으면 됩니다.

TC O(n), SC O(1):
해시셋을 사용하지 않는 방법입니다.
두 링크드리스트에 각각의 포인터를 지정해주고 한칸씩 이동하며 끝지점에 도달할 경우 상대방 노드의 헤드로 이동하게 합니다.
예시의 링크드리스트 둘은 길이의 차이가 있는데 1,3,5,7,9과 2,7,9는 아래와 같이 두 개의 길이차이가 있고
#list a 1-3-5 \
#              7 - 9
#list b     2 /
list a가 1에서 9까지 도달하는데 4회 이동하고 list b의 2로 교차이동하는데 1회 7까지 이동하는데 1회 총 6회의 이동이 필요하며
list b가 9까지 이동하는데 2회 list a의 1로 교차이동하는데 1회 이후 7까지 3회 총 6회의 이동이 필요합니다.
서로 교차하기 때문에 링크드리스트간의 길이차이는 사라지고 곧 만나는 지점이 생기게 되는데 이 부분이 교차점이 됩니다.
"""

from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_list(list: List[int]) -> ListNode:
    if len(list) == 0:
        raise RuntimeError('No elem')
    
    head_node = ListNode(list[0])
    last_node = head_node
    for idx in range(1, len(list)):
        # print(last_node.val, last_node.next)
        node = ListNode(list[idx])
        last_node.next = node
        # print(last_node.val, last_node.next.val)
        last_node = node
    return head_node

def get_idx_node(head: ListNode, idx: int):
    nth_node = head
    for _ in range(0, idx):
        nth_node = nth_node.next
    return nth_node

# intersection 만들어주기
#list a 1-3-5 \
#              7 - 9
#list b     2 /
list1 = create_list([1,3,5,7,9])
list2 = ListNode(2)
intersection = get_idx_node(list1, 3)
list2.next = intersection

class IntersrctionFinder:
    def two_node_way(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        node_a = head_a
        node_b = head_b
        while node_a != node_b:
            if node_a:
                node_a = node_a.next
            else:
                node_a = head_b

            if node_b:
                node_b = node_b.next
            else:
                node_b = head_a
        
        return node_a

    def hash_way(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        hash_set = set()

        current_head = head_a
        while current_head:
            hash_set.add(current_head)
            current_head = current_head.next
        # for i in hash_set:
        #     if i.next != None:
        #         print(i.val, i.next.val)
        #     else:
        #         i.next = 'end_node'
        #         print(i.val, i.next)

        current_head = head_b
        while current_head:
            if current_head in hash_set:
                return current_head.val
            else:
                current_head = current_head.next

        return -1

finder = IntersrctionFinder()

print(finder.two_node_way(list1, list2).val)
print(finder.hash_way(list1, list2))