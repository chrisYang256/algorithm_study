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
        next_node = self.reculsive(node.next)
        if node.value == self.__value:
            return next_node # 이번 값이 삭제할 값이면 다음 노드를 리턴 
        else:
            # 이번 값이 삭제할 값이 아니면 다음 노드와 link
            node.next = next_node 
            return node # 현재 노드 리턴 


nodes = create_list([1,3,5,7,3,1])
print_nodes(nodes)

remover = ElementRemover(1)
recursive_rm = remover.reculsive(nodes)
print_nodes(recursive_rm)