"""
doubly linked list로 구현하는 queue 자료형은 다음과 같습니다.
"""

class QueueNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self._head = QueueNode(-1)
        self._tail = QueueNode(-1)
        self._head.right = self._tail
        self._tail.left = self._head

    def enqueu(self, val: int):
        new_node = QueueNode(val)
        last_node = self._tail.left

        last_node.right = new_node
        new_node.left = last_node

        self._tail.left = new_node
        new_node.right = self._tail

    def dequeqe(self) -> int:
        first_node = self._head.right

        if first_node == self._tail: # 노드 없음
            raise RuntimeError('no elem')

        value = first_node.val
        second_node = first_node.right
        self._head.right = second_node
        second_node.left = self._head

        return value


q = Queue()

q.enqueu(1)
q.enqueu(2)
q.enqueu(3)

print(q.dequeqe())
print(q.dequeqe())
print(q.dequeqe())
print(q.dequeqe())