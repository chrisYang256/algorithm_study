"""
<basic>
두개의 stack을 이용해 FIFO가 되는 stack의 데이터구조를 가진 Q를 만드는 문제입니다.
FIFO 구현을 위해서는 doubly linked list, deque, circular queue를 만드는(가장 끝 노드를 지정할 수 있는) 방법이 있습니다.

enQ -> TC O(1), deQ -> TC O(n) 방법:
2개의 스택을 추가하여 구현할 수 있습니다.
Q에 1,2,3,4가 enQ되면 왼쪽 스택에는 1,2,3,4가 하나씩(O(1)) 순서대로 쌓입니다.
그리고 deQ를 하면 Q에서는 맨 앞의 1이 빠지는데, 스택에서는 1,2,3,4가 들어있는 왼쪽 스택에서 오른쪽 스택에 4,3,2,1의 스택을 넣습니다.
그리고 4를 deQ해준 후 다시 왼쪽 스택에 1,2,3 순서로 넣어줍니다.

enQ -> TC O(1), deQ -> TC amotized O(1) 방법:
! amotized(분할상환) 방식이란 극히 드물게 일어나는 worst case시나리오를 worstCase/n번으로 분할상환한 TC로 생각하라는 말입니다.
추가된 데이터를 하나씩 왼쪽 스택에 쌓고나서 deQ가 일어나면 왼쪽의 맨 위 데이터부터 오른쪽 스택으로 옮기고 
맨 위 데이터를 pop해주는 것 까지는 똑같지만 deQ가 끝나고 다시 왼쪽 스택으로 옮기지 않습니다.
이후 5,6,7이라는 데이터가 들어오면 아래와 같은 스택 모양이 됩니다.
|7|  |3|
|6|  |2|
|5|  |1|
deQ가 3번 일어나면 왼쪽의 스택은 모두 순차적으로 삭제되고 빈 스택이 됩니다.
그리고 다시 deQ가 한 번 일어나면 왼쪽 스택을 7부터 오른쪽 스택으로 옮긴 후 맨 위의 5를 pop해주면 됩니다.
이 경우 왼쪽 스택의 데이터를 오른쪽 스택으로 모두 옮기는 TC O(n)과 pop을 하는 O(1)을 합쳐 O(n)이 됩니다.
그리고 오른쪽 스택에 데이터가 있는 동안 deQ의 TC는 O(1)이 됩니다.
O(1)+O(1)+O(1)+O(n)/n = O(2n)/n = O(1)이 됩니다.
! TC O(n)의 데이터 삽입 동작이 필요하기까지 n번의 TC O(1)를 필요로 하는 deQ들이 있는데 이를 amotized O(1)의 TC를 갖는다고 표현합니다.
! O(n)의 TC를 O(1)+O(1)+O(1)+O(n)만큼 분할해서 상환한다는 개념으로 분할상환이라고 말합니다.
"""

class Q:
    def __init__(self):
        self._push_stack = []
        self._pop_stack = []

    def _move_from_push_to_pop(self): # 왼쪽 스택 들어온 반대 순서로 오른쪽 스택으로 데이터 이동
        while len(self._push_stack):
            v = self._push_stack.pop()
            self._pop_stack.append(v)

    def enQ(self, val:int) -> None:
        self._push_stack.append(val)

    def deQ(self) -> int:
        if len(self._push_stack) == 0 and len(self._pop_stack) == 0:
            raise RuntimeError('no elem')
        if 0 < len(self._pop_stack):
            return self._pop_stack.pop()
        self._move_from_push_to_pop()
        return self._pop_stack.pop()

q = Q()

q.enQ(1)
q.enQ(2)
q.enQ(3)

print(q.deQ())
print(q.deQ())

q.enQ(8)
q.enQ(9)

print(q.deQ())
print(q.deQ())
print(q.deQ())
print(q.deQ())