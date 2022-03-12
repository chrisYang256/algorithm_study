"""
<basic>
두 개의 정렬된 리스트를 합치는 문제입니다.
nodes1 = 1,3,5,7과 nodes2 = 1,2,3,4라는 오름차순으로 정렬된 리스트가 두 개 주어진다면 1,1,2,3,3,4,5를 리턴해야합니다.
각각 리스트의 첫번째 노드를 비교하여 더 작은 경우를 out put list에 넣어주고 선택된 노드를
하나씩 옮겨주면 됩니다.

iterate한 방법을 쓰면 첫 노드를 연결할 대상이 없기 때문에 더미노드를 만들고
current node를 더미노드로 설정한 다음 nodes1과 nodes2를 비교한 후 작은 nodes를 current node에 link한 후
연결한 노드의 포인터를 이동합니다.
그리고 current node는 link된 노드로 변경해 주는 식으로 반복하면 됩니다.
만약 한쪽 노드에 남아있는 노드들이 있다면 이미 오름차순으로 정렬되어 있으므로 current node에 붙여주면 됩니다.
TC는 nodes1: m, list2: n으로 O(m_n)이 되며 각각의 노드1,2가 그 리스트를 하나의 노드씩 체크하며 진행했기 때문입니다.
SC는 더미데이터를 만드는데 드는 O(1)입니다.
"""

from typing import List


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_list(in_list: List[int]) -> ListNode:
    if len(in_list) == 0:
        raise RuntimeError('in_list is empty')
    head_node = ListNode(in_list[0])
    last_node = head_node
    for idx in range(1, len(in_list)):
        node = ListNode(in_list[idx])
        last_node.next = node
        last_node = node
    return head_node

def print_nodes(node: ListNode):
    current_node = node
    while current_node is not None:
        print(current_node.value, end=' ')
        current_node = current_node.next
    print()

class MergeToLists:
    def iterative(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy_node = ListNode(0) # 숫자는 뭐든 상관없음
        current_node = dummy_node

        node1 = list1
        node2 = list2

        while node1 and node2:
            value1 = node1.value
            value2 = node2.value
            if value1 <= value2:
                current_node.next = node1 # 현재 노드에 작은 수의 노드를 link
                current_node = current_node.next # 현재 노드를 link한 노드로 변경
                node1 = node1.next # 다음 노드로 포인터 이동
            else:
                current_node.next = node2
                current_node = current_node.next
                node2 = node2.next
        
        # 남은 노드가 있는 리스트를 이어 붙여줌
        # 정렬되어 있기 때문에 여러개의 노드가 남아있어도 상관없음
        if node1:
            current_node.next = node1
        else:
            current_node.next = node2

        return dummy_node.next

    def recursive(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.value <= list2.value:
            list1.next = self.recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.recursive(list1, list2.next)
            return list2


nodes1 = create_list([1,3,5,7])
nodes2 = create_list([1,2,3,4])
# print_nodes(nodes1)
# print_nodes(nodes2)

merge = MergeToLists()
# iterative_merge = merge.iterative(nodes1, nodes2)
# print_nodes(iterative_merge)

recursive_merge = merge.recursive(nodes1, nodes2)
print_nodes(recursive_merge)