"""
<basic>
1,3,5,7,9인 링크드리스트를 9,7,5,3,1로 역배치 하는 문제입니다.

TC O(n), SC O(1):
previouse, current, next 3개의 포인터를 이용하여 3개의 노드를 지정하고 노드들의 next를 바꿔주는 방법입니다.
cur노드의 next를 prev로 바꾸고 prev는 cur노드 자리로 이동하고 cur노드는 next노드의 자리로 이동한 후 
next노드는 cur노드가 가리키는 다음 노드로 이동하며 이 동작을 반복하면 cur노드가 아무것도 가리키지 않게 되는 때
prev노드를 리턴시켜줍니다.
원래 첫 노드의 next를 처리하지 못한 edge case는 코드로 아무것도 가리키지 않게 지정해주면 됩니다.

recursive way:
해당 노드가 가리키는 next의 next를 자기 자신으로 바꾸는 방법입니다.
TC는 n개의 함수를 불렀기 때문에 O(n), SC는 n개의 스택이 쌓여야하므로 O(n)이 됩니다.
"""

import re
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
        node = ListNode(list[idx])
        last_node.next = node
        last_node = node
    return head_node

def print_nodes(nodes: ListNode) -> int:
    current_node = nodes
    while current_node:
        print(current_node.val, end=' ')
        current_node = current_node.next
    print()


class ReverseList:
    def iterative_way(self, head: ListNode) -> ListNode:
        if head is None:
            return RuntimeError('No head')
        elif head.next is None:
            return head

        prev = head
        curr = head.next
        head.next = None # 역정렬 될 첫번째 노드의 next 삭제

        while curr:
            temp_next_node = curr.next 
            curr.next = prev # next를 앞의 노드로 변경
            prev = curr # 이동
            curr = temp_next_node

        return prev

    def reculsive_way(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        elif head.next is None:
            return head

        back_head = self.reculsive_way(head.next)
        head.next.next = head
        head.next = None

        return back_head

list1 = create_list([1,3,5,7,9])
list2 = create_list([1,3,5,7,9])
# print_nodes(list1)

reverse = ReverseList()
print_nodes(reverse.iterative_way(list1))

print_nodes(reverse.reculsive_way(list2))