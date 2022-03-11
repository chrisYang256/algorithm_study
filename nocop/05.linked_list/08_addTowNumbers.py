"""
<basic>


<middle>

"""

from turtle import forward
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
        dummy_node = ListNode(-1)
        curr_node = dummy_node
        node1 = list1
        node2 = list2
        carry = 0

        while node1 or node2:
            num1 = node1.val if node1 else 0
            num2 = node2.val if node2 else 0
            sum12 = num1 + num2 + carry
            carry = sum12 // 10
            val = int(sum12 % 10)

            new_node = ListNode(val)
            curr_node.next = new_node
            curr_node = curr_node.next
            node1 = node1.next if node1 else None
            node2 = node2.next if node1 else None

        if 1 == carry:
            new_node = ListNode(carry)
            curr_node.next = new_node

        return dummy_node.next

    def add_forward(self, list1: ListNode, list2: ListNode) -> ListNode:
        reverse_head1 = self.__reverse_list(list1)
        reverse_head2 = self.__reverse_list(list2)
    
        reverse_sum = self.add_reverse(reverse_head1, reverse_head2)
        forward_sum = self.__reverse_list(reverse_sum)
        return forward_sum

    def __reverse_list(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        elif head.next is None:
            return head

        curr_node = head.next
        prev_node = head
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