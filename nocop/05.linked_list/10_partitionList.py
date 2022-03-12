"""
<middle>
1,7,5,3,6,3과 x=5가 주어졌을 때 5보다 작은 수는 왼쪽에, 큰 수는 오른쪽에 배치하되 노드들의 순서는 바꾸지 않게 정렬하는 문제입니다.
링크드리스트의 가장 큰 장점인 node의 next를 자유롭게 변경할 수 있다는 점을 이용하면 됩니다.

x < 리스트와 x > 리스트를 만들고 각 리스트에 더미노드를 생성해줍니다.
그리고 메인 리스트에 current포인터를 주고 순회하며 x보다 작은 경우 x < 리스트와 연결해주는 식으로 진행하면
current포인터가 순회를 마치며 첫번째 파티셔닝이 종료됩니다.
그리고 x < 리스트 마지막 노드의 next를 x > 리스트의 더미노드.next(첫번째노드)에 연결해주면 됩니다.
TC는 순회하는데 O(n), SC는 만든게 없기 때문에 O(1)이 됩니다.
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

def print_nodes(head: ListNode):
    cur_node = head
    while cur_node:
        print(cur_node.val, end=' ')
        cur_node = cur_node.next
    print()

class Partitioner:
    def two_list_way(self, head: ListNode, x: int) -> ListNode:
        dummy_node1 = ListNode(-1) # x보다 작은쪽
        dummy_node2 = ListNode(-1)

        node1 = dummy_node1 # x보다 작은쪽 리스트 생성
        node2 = dummy_node2

        cur_node = head # 원본 링크드리스트
        while cur_node:
            val = cur_node.val
            if x <= val:
                node2.next = cur_node
                node2 = node2.next
                cur_node = cur_node.next
            else:
                node1.next = cur_node
                node1 = node1.next
                cur_node = cur_node.next

        node2.next = None
        node1.next = dummy_node2.next # 작은쪽 마지막 노드에 큰쪽 실재 head 연결

        return dummy_node1.next

partition = Partitioner()

list1 = create_node([1,3,7,5,3,6])
x = 5

partitioned = partition.two_list_way(list1, x)
print_nodes(partitioned)
