"""
<basic>
링크드리스트에서 특정 노드들을 삭제하는 문제입니다.
after remove는 삭제할 노드 앞에 노드가 존재해야하는 조건 때문에 첫 노드가 삭제 대상일 경우 edge case가 생깁니다.
따라서 previous 노드가 없는 경우에는 재귀를 통해 reculsive한 방법을 사용합니다.

만약 iterative한 방법으로 문제를 해결하려 한다면
head node 앞에 dummy node를 두어서 첫 노드가 삭제 대상인 edge case를 해결할 수도 있습니다.
그리고나서 curr node가 삭제할 값을 만날 때마다 prev node를 curr node와 연결시켜주기만 하면 됩니다.
마지막으로 남은 노드의 시작점을 리턴해야 하는데 dummy.next를 리턴하면 이 시작점이 곧 head가 되고
이전 dummy node는 언어에 따라 자동으로 삭제되던 수동으로 삭제하던 처리하면 됩니다.
TC는 더미 노드를 만드는 O(1), iterate 하는 O(n), 새로운 시작점을 pointing하는 O(1)로 총 O(n)이 필요하고
SC는 더미 노드를 만드는데 O(1)이 필요합니다.
"""

from multiprocessing import dummy
from typing import List


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_list(in_list: List[int]) -> ListNode:
    if len(in_list) == 0:
        raise RuntimeError('in_list is empty')
    head_node = ListNode(in_list[0]) # 헤드 미리 지정
    last_node = head_node # 최초에 노드가 헤드 하나뿐이기 때문에 처음이자 마지막 노드이므로 뒤에 노드를 붙이기 위해 우선 last node가 됨
    for idx in range(1, len(in_list)): # 헤드 뒤로 노드 연결
        node = ListNode(in_list[idx])
        last_node.next = node # 앞 노드의 next로 다음 노드를 link
        last_node = node # 이제 현재 노드가 last node가 됨
    return head_node # 프린트든 뭐든 처음부터 시작해야 하므로 헤드를 리턴

def print_nodes(node: ListNode):
    current_node = node
    while current_node is not None:
        print(current_node.value, end=' ')
        current_node = current_node.next
    print()


class ElementRemover:
    def __init__(self, value):
        self.__value = value # 변수 앞에 __가 있는 경우 선언된 클래스 안에서만 해당 이름으로 사용 가능

    def reculsive(self, node: ListNode) -> ListNode:
        if not node:
            return None
        next_node = self.reculsive(node.next) # 재귀로 다음 노드를 호출 / 리턴
        if node.value == self.__value:
            return next_node # 이번 값이 삭제할 값이면 next_node를 이전 노드에게 넘겨줌
        else:
            # 이번 값이 삭제할 값이 아니면 next node를 다음 노드로 넣어줌
            # 만약 이전 노드가 삭제할 노드였다면 next_node는 삭제할 노드의 다음 노드인 상태이고 아래 식으로 삭제할 노드는 삭제됨 
            node.next = next_node 
            return node # 현재 노드 리턴 

    def iterative(self, node: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = node # 첫 노드가 삭제할 노드인 경우의 edge case

        current_node = node
        previous_node = dummy_head
        while current_node:
            if current_node.value == self.__value:
                previous_node.next = current_node.next # 앞 노드에 뒷 노드를 연결(현재 노드를 삭제)
                current_node = current_node.next
            else: # 삭제할 노드가 아니면 포인터만 옮기면 됨
                previous_node = previous_node.next
                current_node = current_node.next
        return dummy_head.next # 더미헤드는 제외


nodes = create_list([1,3,5,1,3,1])
print_nodes(nodes)

remover = ElementRemover(1)
recursive_rm = remover.reculsive(nodes)
print_nodes(recursive_rm)
# iterative_rm = remover.iterative(nodes)
# print_nodes(iterative_rm)