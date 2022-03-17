"""
<basic>
Q에서 가장 큰 값을 리턴하는 문제입니다.

Q에 숫자가 enQ될 때마다 max값을 식별하는데 필요한 추가 데이터스트럭쳐에 가장 큰 enQ값을 넣고 
가장 큰 값을 찾을 때 여기서 리턴해주면 O(1)이 가능합니다.
1이 들어오면 Q와 max에 넣습니다.
이어서 5가 들어오면 Q에 enQ하고 max에서는 5보다 작은값인 1을 삭제하고 5를 넣습니다.
뒤이어 3,3이 들어오면 Q에 enQ해주고 max에는 5에 뒤이어 3,3을 넣어줍니다.
이제 deQ를 했을 때 Q에는 1이 빠지고 max에는 5가 1보다 크기 때문에 아무 동작도 하지 않습니다.
이후 다시 deQ를 하면 Q에서 5를 빼고 max에 있는 5와 같기 때문에 max에서도 5를 제거해줍니다.
이 상태에서 max값은 max의 첫번째 elem인 3이 됩니다.
이제 7이 들어오면 Q에 넣어주고 max에서는 3과 7을 비교해 7이 더 크므로 3을 삭제하고 하나 더 있는 3역시 삭제 후 7을 넣어줍니다.
주의할 점은 Q에서는 데이터가 나가는 앞쪽에는 Out을, 데이터가 들어오는 뒷쪽에는 in을 구현해주면 되는데
max에서는 앞쪽에 데이터가 나가는 out을 구현하고 뒷쪽에서는 데이터가 들어가고 나갈 수 있도록 in과 out 모두 넣어줘야 한다는 것입니다.

TC는 max에서 첫번째 데이터만 리턴해주면 되므로 O(1)이, deQ는 Q의 맨 앞 데이터를 빼면서 비교가 일어나는데
max의 맨 앞의 데이터와 한 번만 비교해주면 되기 때문에 O(1)이 됩니다.
enQ는 Q의 맨 뒤에 들어가게 되면서 max의 데이터들(o(n))과 비교하게 되는데 분할상환적(amortized) 관점에서 봤을 때 amortized O(1)이 됩니다.

deque(데크):
보통 큐(queue)는 선입선출(FIFO) 방식으로 동작하는 반면, 양방향 큐가 있는데 그것이 바로 데크(deque)로
앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있으며 양 끝 엘리먼트의 append와 pop이 압도적으로 빠릅니다.
컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 
일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 데크(deque)는 O(1)로 접근 가능합니다.
- deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
- deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
- deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- deque.remove(item): item을 데크에서 찾아 삭제한다.
- deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

simple queue:
상한 없는 FIFO 큐의 생성자. 단순 큐에는 작업 추적과 같은 고급 기능이 없습니다.
- SimpleQueue.qsize()
    큐의 대략의 크기를 돌려줍니다. 주의하십시오, qsize() > 0 은 후속 get()이 블록 되지 않는다는 것을 보장하지 않습니다.
- SimpleQueue.empty()
    큐가 비어 있으면 True를, 그렇지 않으면 False를 반환합니다. 
    empty()가 False를 반환하면, get()에 대한 후속 호출이 블록 되지 않는다는 것을 보장하지는 않습니다.
- SimpleQueue.put(item, block=True, timeout=None)
    item을 큐에 넣습니다. 
    이 메서드는 결코 블록하지 않고 항상 성공합니다(메모리 할당 실패와 같은 잠재적 저수준 에러 제외). 
    선택적 인자 block과 timeout은 무시되고 Queue.put()과의 호환성을 위해서만 제공됩니다.
- SimpleQueue.put_nowait(item)
    put(item)과 동등합니다, Queue.put_nowait()와의 호환성을 위해 제공됩니다.
- SimpleQueue.get(block=True, timeout=None)
    큐에서 항목을 제거하고 반환합니다. 
    선택적 인자 block이 참이고 timeout이 None(기본값)이면, 항목이 사용 가능할 때까지 필요하면 블록합니다. 
    timeout이 양수면, 최대 timeout 초 동안 블록하고 그 시간 내에 사용 가능한 항목이 없으면 Empty 예외가 발생합니다. 
    그렇지 않으면 (block이 거짓), 즉시 사용할 수 있는 항목이 있으면 반환하고, 
    그렇지 않으면 Empty 예외를 발생시킵니다(이때 timeout은 무시됩니다).
- SimpleQueue.get_nowait()
    get(False)와 동등합니다.
"""

from collections import deque
import queue


class MaxQ:
    def __init__(self):
        self._data = queue.SimpleQueue()
        self._max = deque()

    def max(self):
        return self._max[0]

    def enQ(self, val:int):
        self._data.put(val)
        while 0 < len(self._max) and self._max[-1] < val: # val이 3이고 max가 5면 멈추고 max.append(3) -> [5,3]
            self._max.pop()
        self._max.append(val)
        # print('enQ:::', self._data.qsize(), self._max)

    def deQ(self):
        val = self._data.get()
        # Q의 val이 max[0]보다 작은 경우는 이미 enQ()에서 삭제되었고,
        # max[0]은 enQ()에서 이미 가장 큰 수로 지정되었기 때문에 deQ되는 데이터가 Q에서 가장 큰 수인 경우는 max에서도 가장 큰 수
        if val == self._max[0]:
            self._max.popleft()
        # print('deQ:::', self._data.qsize(), self._max)
        return val

maxQ = MaxQ()

maxQ.enQ(1)
print('Q = [1], ', 'max:::', maxQ.max())
maxQ.enQ(4)
print('Q = [1,4], ', 'max:::', maxQ.max())
maxQ.enQ(2)
print('Q = [1,4,2], ', 'max:::', maxQ.max())
maxQ.enQ(3)
print('Q = [1,4,2,3], ', 'max:::', maxQ.max())

print('deQ:::', maxQ.deQ())
print('max:::', maxQ.max())

print('deQ:::', maxQ.deQ())
print('max:::', maxQ.max())