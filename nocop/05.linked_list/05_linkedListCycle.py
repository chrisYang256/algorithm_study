"""
<basic>
[1,3,5,7,9]이라는 노드 리스트에 루프가 있는지 확인하는 문제입니다.

hash set 사용:
노드 리스트를 순회하며 hash set에 


"""

from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_node(list: List[int]) -> ListNode:
    if len(list) == 0:
        return RuntimeError('no elem')
    
    head_node = ListNode(list[0])
    last_node = head_node
    for idx in range(1, len(list)):
        node = ListNode(list[idx])
        last_node.next = node
        last_node = node
    return head_node

def make_loop(head: ListNode, start_node_idx: int):
    end_node = head
    while end_node.next: # 루프 끝점이 노드 리스트의 끝
        end_node = end_node.next

    current_node = head
    for _ in range(1, start_node_idx): # current_node가 지정되어 있기 때문에 루프 시작 idx가 2면 1번만 움직이면 됨
        current_node = current_node.next
    end_node.next = current_node # 끝 노드와 연결하여 루프 완성

class HasLoop:
    def hash_way(self, head: ListNode) -> bool:
        if head is None:
            return False

        node_set = set() 
        current_node = head
        while current_node:
            if current_node in node_set:
                return True # 마지막 노드의 next가 가리키는 node가 앞서 hash set에 들어와 있다면 루프가 존재하는 것이므로
            node_set.add(current_node)
            current_node = current_node.next # 마지막 노드가 next를 가지고 있다면 위에서 True가 됨

        return False

    def slow_fast(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        slow_node = head
        fast_node = head
        while fast_node:
            if fast_node.next:
                slow_node = slow_node.next
                fast_node = fast_node.next.next
            else:
                break

            if fast_node == slow_node:
                return True
            
        return False

nodes = create_node([1,3,5,7,9])
make_loop(nodes, 2)

has_loop = HasLoop()
print(has_loop.hash_way(nodes))
print(has_loop.slow_fast(nodes))