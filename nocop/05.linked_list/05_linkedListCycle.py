"""
<basic>
[1,3,5,7,9]이라는 노드 리스트에 루프가 있으면 True를 반환하는 문제입니다.

hash set 사용:
노드 리스트를 순회하며 현재 노드가 hash set에 없는 경우 넣어두고 다음 노드로 포인트를 옮기는데
만약 다음 노드가 set 안에 있다면 루프가 형성되어있다는 의미이므로 True가 됩니다.
TC는 노드를 순회하는 O(n)이, SC는 hash set을 저장하는 O(n)이 필요하게 됩니다.

fast & slow pointer:
각각 한칸씩 이동하는 포인터와 두칸씩 이동하는 포인터를 만들고 순회시키면 만약 루프가 존재하는 경우
두 포인터가 루프 안에서 돌게 되고 언젠가 서로 만나게 되므로 루프가 존재한다는 증명이 됩니다.
fast.next가 존재하지 않는 경우 반복을 종료하게 되는 조건을 걸고 반복이 종료된다면 루프가 없다는 의미가 됩니다.
TC는 fast 포인터가 루프시작점에 도달하는 시간 O(n) + fast가 slow를 잡는데 걸리는 시간 O(k)가 되고 k = 루프 안 노드의 갯수인데 
k가 가질 수 있는 최대 노드의 갯수를 n이 되기 때문에 O(n) + O(n) 즉, 최종 TC는 O(n)이 됩니다.
SC는 추가 공간을 사용하지 않았기 때문에 O(1)이 됩니다.
"""

from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_node(list: List[int]) -> ListNode:
    if len(list) == 0:
        raise RuntimeError('no elem')
    
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
            else: # 루프가 존재하지 않으면 node.next가 있을 수 없으므로 False
                break

            if fast_node == slow_node:
                return True
            
        return False

nodes = create_node([1,3,5,7,9])
make_loop(nodes, 2)

has_loop = HasLoop()
print(has_loop.hash_way(nodes))
print(has_loop.slow_fast(nodes))