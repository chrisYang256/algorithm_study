"""
<singly linked list implementation>
실재 코딩테스트에서는 아래와 같은 링크드리스트의 오브젝트 그 자체가 주어지는 것이 아니라
이미 만들어진 링크드리스트의 head node만 주어집니다.
또한 아래 implementation은 몇개의 edge case는 생략하였습니다.
"""

from locale import currency


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_nodes(node: ListNode):
    current_node = node
    while current_node is not None:
        print(current_node.value, end=' ')
        current_node = current_node.next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 현재 어떠한 요소가 들어있던 새로운 노드를 만들고 링크들을 재정렬하면 되므로 O(1)
    def add_at_head(self, value):
        node = ListNode(value)
        node.next = self.head
        self.head = node

    # 현재 노드를 옮기며 마지막에 새로운 노드를 추가하므로 O(n)
    def add_back(self, value): # 맨 뒤에 노드 추가
        node = ListNode(value)
        if self.head is None: # 앞에 노드가 없는 경우 자신이 첫번째 노드가 되도록
            node.next = self.head
            self.head = node
            return
        current_node = self.head # 현재 노드를 헤드부터 시작
        while current_node.next: # 현재 노드가 next value를 가지고 있을 때 까지 노드의 위치를 끝으로 옮김
            current_node = current_node.next
        current_node.next = node # next value가 없는 마지막 노드에 현재 노드를 연결

    # 특정 노드를 찾기 위해 순회하므로 O(n)
    def find_node(self, value): # 특정 노드 찾기
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        raise RuntimeError('Node not found')
    
    # 찾고자 하는 노드의 정보가 들어왔기 때문에 새로운 노드만 삽입하고 링크를 정렬하면 되므로 O(1)
    def add_after(self, node, value): # 특정 노드 뒤에 노드 추가
        new_node = ListNode(value)
        new_node.next = node.next # 원래 앞 노드가 가리키던 다음 노드를 새로운 노드가 가리키게 
        node.next = new_node # 앞 노드가 새로운 노드를 가리키게

    # 노드의 정보가 들어왔기 때문에 노드 삭제 / 링크 연결만 하면 되므로 O(1)
    def delete_after(self, prev_node): # prev_node 뒤의 노드를 삭제
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next # 삭제할 노드 뒤 노드와 prev_node 연결
            # c++, python 등 unmanaged memory 언어는 삭제된 노드를 수동으로 삭제시켜줘야함

slist = SinglyLinkedList()
slist.add_at_head(1)
slist.add_at_head(2)
slist.add_back(3)
find_node1 = slist.find_node(1)
# find_fail = slist.find_node(0)
slist.add_after(find_node1, 7)
print_nodes(slist.head)
print('')
slist.delete_after(find_node1)
print_nodes(slist.head)