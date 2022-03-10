"""
<basic>
노드의 중간지점 노드를 리턴해주는 문제입니다.
1,3,5,7,9가 있다면 5,7,9를, 1,2,3,4,가 있다면 3,4을 리턴(2와 3 사이면 3을 선택)해주면 됩니다.

카운트 변수와 current 포인터를 만들어 포인터가 노드를 순회하며 노드의 갯수를 알아낸 후 
절반으로 나눈 만큼 current 포인트를 처음으로 이동시킨 후 나눈 값 만큼 이동하여 그 노드를 리턴하는 방법이 있습니다.
TC O(n), SC O(1)입니다.

한 번의 iterate로 해결(one pass)하는 방법으로는
노드를 배열로 만든 후 배열 길이의 절반값으로 바로 찾는 방법입니다.
TC는 노드를 배열에 넣는데 필요한 O(n), SC는 노드를 배열에 넣는데 필요한 O(n)이 됩니다.
SC를 O(1)로 풀기 위해서는 slow_pointer와 past_pointer 두개를 만들고 각각 1칸, 2칸씩 이동하게 하여
past_pointer가 종료되는 시점이 slow_pointer가 중간이 되는 시점임을 이용하는 방법이 있습니다.
"""

from typing import List


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_list(list: List[int]) -> ListNode:
    if len(list) == 0:
        return RuntimeError('list is empty')
    head_node = ListNode(list[0])
    last_node = head_node

    for idx in range(1, len(list)):
        node = ListNode(list[idx])
        last_node.next = node
        last_node = node
    return head_node

def print_nodes(node: ListNode):
    current_node = node
    while current_node:
        print(current_node.value, end=' ')
        current_node = current_node.next
    print()

class MiddleNode:
    def index_way(self, head: ListNode) -> ListNode:
        total_count = 0
        current_node = head
        while current_node:
            total_count += 1
            current_node = current_node.next
        
        half_count = total_count//2

        current_node = head
        for _ in range(0, half_count):
            current_node = current_node.next

        return current_node

    def array_way(self, head: ListNode) -> ListNode:
        node_array = []
        current_node = head

        while current_node:
            node_array.append(current_node)
            current_node = current_node.next
        half_count = len(node_array)//2
        # print(node_array)
        return node_array[half_count]

    def fast_slow(self, head: ListNode) -> ListNode:
        fast_node = head
        slow_node = head

        while fast_node:
            if fast_node.next:
                fast_node = fast_node.next.next
                slow_node = slow_node.next
            else:
                break

        return slow_node

nodes = create_list([1,3,5,7,9])
print_nodes(nodes)

middle = MiddleNode()

index = middle.index_way(nodes)
print_nodes(index)
array = middle.array_way(nodes)
print_nodes(array)
tow_point = middle.fast_slow(nodes)
print_nodes(tow_point)