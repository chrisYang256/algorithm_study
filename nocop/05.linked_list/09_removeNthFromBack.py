"""
<middle>
1,2,5,7,9와 n=2 주어졌을 때 뒤에서 두번째인 7을 삭제하는 문제입니다.

two pass counter:::
링크드 리스트를 순회하여 아렉된 길이에서 n을 뺀 수만큼 다시 처음부터 이동하여 해당 숫자를 찾는 방법입니다.
노드가 1개만 있는 엣지 케이스는 헤드를 삭제해줘야 하는데 이것은 더미노드를 만들어 헤드를 삭제시키고
dummy node가 가리키는 null이나 none을 리턴하면 됩니다.
대부분의 링크드리스트 문제는 더미노드가 필요하다는 것을 알 수 있습니다.
TC는 길이를 알기 위한 순회 O(n), SC는 O(1)이 됩니다.

array:::
링크드리스트의 각각의 노드가 포인터 혹은 reference입니다.
주어진 링크드리스트를 더미노드와 함께 각각의 포인터 레퍼런스를 arr에 넣을 수 있습니다.
1,2,5,7,9과 더미노드를 포함하여 6개의 노드가 있고 삭제 대상이 끝에서 2번째인 idx 4라는 것을 바로 알 수 있습니다.
이후 삭제할 노드 앞의 노드의 next를 삭제할노드 뒤의 노드와 연결시키고 헤드노드를 리턴시켜주면 됩니다.
TC는 순회하는데 O(n), SC는 arr를 만드는데 O(1)이 필요합니다.

two node, one pass:::
first노드를 더미노드에 할당하고 k만큼 이동시킨 후 second노드를 더미노드에 할당합니다.
최초 각각의 위치는 idx를 비유하여 first는 2, second는 0이 됩니다.(k=2의 경우 first가 두칸 앞)
그리고 함께 움직이다가 first노드가 끝지점에 다다르면 second노드의 next를 second.next.next에 연결해주면 됩니다.
TC는 순회하는데 O(n), SC는 n(1)이 됩니다.
"""

from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_list(list: List[int]) -> ListNode:
    if len(list) == 0:
        raise RuntimeError('no elem')

    head_node = ListNode(list[0])
    last_node = head_node
    for idx in range(1, len(list)):
        node = ListNode(list[idx])
        last_node.next = node
        last_node = node
    return head_node

def print_nodes(head: ListNode):
    current_node = head
    while current_node:
        print(current_node.val, end=' ')
        current_node = current_node.next
    print()

class RemoveNthBack:
    def count_way(self, head: ListNode, nth: int) -> ListNode:
        if nth == 0:
            return head

        count = 0
        current_node = head
        while current_node:
            count += 1
            current_node = current_node.next

        destination = count - nth
        dummy_node = ListNode(-1) # list 1개일 경우를 대비, nth가 1 이상이면 head를 삭제시키고 더미노드의 next인 null이나 none을 리턴
        dummy_node.next = head
        current_node = dummy_node
        for _ in range(0, destination): # 삭제할 노드 앞 노드까지 포인터 이동
            current_node = current_node.next

        current_node.next = current_node.next.next # del/new link
        return dummy_node.next

    def arrayApproach(self, head: ListNode, nth: int) -> ListNode:
        if nth == 0:
            return head

        dummy_node = ListNode(-1)
        dummy_node.next = head
        cur_node = dummy_node
        node_list = []
        while cur_node:
            node_list.append(cur_node)
            cur_node = cur_node.next
            
        del_idx = len(node_list) - nth
        prev_idx = del_idx - 1
        prev_node = node_list[prev_idx]
        prev_node.next = prev_node.next.next # del/new link

        return dummy_node.next

    def two_pointers(self, head: ListNode, nth: int) -> ListNode:
        if nth == 0:
            return head

        dummy_node = ListNode(-1)
        dummy_node.next = head
        first_node = dummy_node

        for _ in range(0, nth+1): # 0,1,2 -> 3칸 이동
            first_node = first_node.next
        
        second_node = dummy_node
        while first_node:
            first_node = first_node.next
            second_node = second_node.next

        second_node.next = second_node.next.next
        return dummy_node.next


list1 = create_list([1,3,5,7,9])
list2 = create_list([1,3,5,7,9])
list3 = create_list([1,3,5,7,9])
k = 2

rm_back = RemoveNthBack()

print_nodes(rm_back.arrayApproach(list1, k))
print_nodes(rm_back.count_way(list2, k))
print_nodes(rm_back.two_pointers(list3, k))