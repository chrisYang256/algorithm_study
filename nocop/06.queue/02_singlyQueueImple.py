"""
singly linked list로 구현하는 queue 자료형은 다음과 같습니다.
boubly보다 메모리를 적게 사용하는 장점이 있습니다.
기본적인 싱글로는 head 앞의 데이터 추가삭제에 대해서만 O(1)을 갖고 dequeue의 경우 순회해야 하기 때문에 O(n)이 됩니다.
이 문제는 싱글 리스트의 마지막 노드를 reference노드로 관리하면 됩니다.
last노드 포인터가 항상 리스트의 마지막을 가리키게 하고 새로운 데이터가 enqueue되면
last노드 뒤에 이어주고 last노드를 이어준 노드로 바꿔주면 O(1)이 됩니다.
리스트에 헤드노드가 하나만 있는 경우에 대한 엣지케이스 처리도 잊지 말아야합니다.
"""

class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self._head = Node(-1)
        self._last = self._head # Point: 라스트 노드 지정

    def enqueue(self, val:int):
        new_node = Node(val)

        self._last.next = new_node # 라스트 노드 갱신
        self._last = new_node

    def dequeue(self): # 노드값 출력 / 노드 삭제
        if self._last == self._head: # 헤드노드 제외 노드가 없음
            raise RuntimeError('no elem')

        first_node = self._head.next
        value = first_node.val
        if first_node == self._last: # 현재 헤드노드를 제외한 노드가 1개뿐일 때
            self._last = self._head 
            return value

        self._head.next = first_node.next
        return value

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())