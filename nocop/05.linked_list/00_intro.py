class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# 노드 생성
head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)

# 노드 프린트
# iterative한 방법
def print_iterative(node: ListNode):
    current_node = node
    while current_node is not None:
        print(current_node.value, end=' ')
        current_node = current_node.next

print_iterative(head_node)

# recursive한 방법
def print_recursice(node: ListNode):
    print(node.value, end=' ')
    if node.next is not None:
        print_recursice(node.next)

print(print_recursice(head_node))