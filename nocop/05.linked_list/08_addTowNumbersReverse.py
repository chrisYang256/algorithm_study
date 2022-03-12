"""
<basic> - reverse
reverse는 링크드리스트 문제를 훨씬 쉽게 만들어주는 장치입니다.
7,5,3과 4,8,2 두개의 링크드리스트가 주어졌을 때 뒷자리부터 즉, 357 + 284 더하여 나온 값을 역순으로 리턴해야 합니다.
3,5,7,
2,8,4
위의 경우 덧셈을 하면 뒷자리부터 시작하여 올림이 있게 되고 방향은 "<-" 가 되고 641이 되며 146을 리턴하면 됩니다.
7,5,3
4,8,2
그냥 앞에서부터 더하면서 두자리숫자(올림)이 있는 경우 다음으로 패스해주면 쉽습니다.
원래 링크드리스트 순서 그대로인 상태에서 "->"방향으로 더해주고 올림을 해주면 되기 때문에 간단한 문제가 됩니다.
7+4는 11이고 1을 써주고 1을 올려줍니다. -> 5+8에 올려준 1을 더해 14가 되면 4를 쓰고 1을 올립니다. -> 3+2에 올려준 1을 더해 6을 씁니다.
올리는 값이 발생하는 경우 변수에 저장하고, dummy node를 만들어 계산하며 연결해주는 것을 반복하면 됩니다.
TC는 m=7,5,3, n=4,8,2로 O(max(m,n))이 되고 SC는 따로 할당받는 공간이 없으므로 n(1)이 됩니다.

<middle> - no reverse
reverse가 없어지면서 난이도가 상승합니다.
7,5,3 + 4,8,2를 구하여 1,2,3,5를 리턴해야 합니다.
reverse linked list로 역방향으로 노드를 정렬하고 add two numbers reverse로 합을 구한 다음 다시 reverse linked list로 정렬하면 됩니다.
"""

from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def create_list(list: List[int]) -> ListNode:
    if len(list) == 0:
        return RuntimeError('no elem')
    
    head_node = ListNode(list[0])
    last_node = head_node
    for idx in range(1, len(list)):
        node = ListNode(list[idx])
        last_node.next = node
        last_node = node
    return head_node

def print_nodes(node: ListNode):
    curr_node = node
    
    while curr_node:
        print(curr_node.val, end=' ')
        curr_node = curr_node.next
    print()

class ListAdder:
    def add_reverse(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 계산 결과를 저장할 노드 생성 / 연결 대상이 필요하므로 더미를 생성하는 것임
        # 아래 while문 안에 if curr_node is not: ListNode(val)같이 해도 되지만 가독성 저하 / 반복문에 의해 불필요연산이 증가함
        dummy_node = ListNode(-1)
        curr_node = dummy_node
        node1 = list1 # 보통 헤드가 항상 첫 대상이라는 것을 잊지말자
        node2 = list2
        carry = 0

        while node1 or node2:
            num1 = node1.val if node1 else 0
            num2 = node2.val if node2 else 0
            sum12 = num1 + num2 + carry
            carry = sum12 // 10
            val = int(sum12 % 10) # 뒷자리만

            new_node = ListNode(val)
            curr_node.next = new_node  # 뒷자리를 앞 노드에 연결해주고
            curr_node = curr_node.next # 다음 자릿수로 갱신
            node1 = node1.next if node1 else None
            node2 = node2.next if node1 else None

        if carry == 1: # 반복문 후 올림이 있으면 연결
            new_node = ListNode(carry)
            curr_node.next = new_node

        return dummy_node.next

    def add_forward(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 처리방식을 add to numbers reverse와 같게 만들기 위해서 리스트 역정렬
        reverse_head1 = self.__reverse_list(list1) # 3,5,7
        reverse_head2 = self.__reverse_list(list2) # 2,8,4
    
        reverse_sum = self.add_reverse(reverse_head1, reverse_head2) # 5,3,2,1
        forward_sum = self.__reverse_list(reverse_sum) # 1,2,3,5
        return forward_sum

    def __reverse_list(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        elif head.next is None:
            return head

        prev_node = head
        curr_node = head.next
        head.next = None

        while curr_node:
            temp_next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_next_node

        return prev_node

list1 = create_list([7,5,3])
list2 = create_list([4,8,2])
list3 = create_list([7,5,3])
list4 = create_list([4,8,2])

adder = ListAdder()

print_nodes(adder.add_reverse(list1, list2))
print_nodes(adder.add_forward(list3, list4))