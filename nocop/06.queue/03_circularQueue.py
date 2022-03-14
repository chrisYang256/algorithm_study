"""
<basic>
실무에서 매우 많이 사용되는 data structure입니다.
일반적인 큐는 [1,3,5,7]이 있을 때 1이 front, 7이 rear이 됩니다.
그리고 dequeue가 발생하면 [3,5,7]이 되고 front는 3으로 변경됩니다.

서큘러큐역시 삭제되는 경우 front나 rear가 바뀌는데 
차이점은 동그란 모양이므로 곧 갯수 제한이 있다는 의미로 갯수를 초과하는 엔큐가 발생하면 overflow가 됩니다.
  /-----------\
 |      1      |
|  7    •    3  |  -> 여기서 디큐/엔큐가 한 번씩 일어나면 1은 삭제되고 front는 3으로 바뀝니다.
 |      5      |
  \-----------/
컴퓨터 메모리는 이러한 동그란 데이터구조가 아니므로 우리는 Linear data structure를 이용해야 합니다.
서큘러큐가 [1,2,3,4]이고 데이터 입력 제한이 4일 때 
deQ가 두번 되면 Q는 [ , , 3, 4]가 되고 프론트는 3, rear는 4이 됩니다.
이 상태에서 5,6 데이터가 입력되면 원의 형태라고 생각하고 max idx를 초과하기 때문에 첫 idx로 돌아가서
데이터를 채우고 [5, 6, 3, 4]가 되고 front는 4, rear는 6이 됩니다.
!여기서 헷갈림에 주의해야 할 점은 dequeue는 fornt가, enqueue는 rear가 이동한다는 것인데
먼저 들어온 데이터 순서를 구분하기 위해 데이터를 추가하는 경우 마지막에 들어온 데이터를 rear가 가리키도록 만들어야 하기 때문입니다.(FIFO)
서큘러를 구현하기 위해서 idx를 계산해야 하는데 circularQ의 idx % 포인터의 현재idx로 나머지가 0이 되면 
포인터를 idx 0으로 보내주면 됩니다.

!circular queue의 핵심은 idx가 갱신될 때마다 나머지를 계산한다는 점입니다.

circulerQ의 장점: 
링크드리스트로 구현한 Q의 random idx는 n(n)인데 반해 circulerQ는 n(1)로 idx에 접근 가능.
1d array가 가지는 잇점은 memory가 연속적이게 data가 들어있어서 cache hit이 계속해서 나옴.
결론적으로 Q와 circulerQ를 비교하기보다 circulerQ의 뒷단이 array나 list인 경우 여러 장점이 생김.
"""

class CircularQ:
    def __init__(self, k:int):
        self._data = [None] * k # 데이터 입력제한 갯수 세팅 / 데이터 입력-삭제 포인터
        self._size = 0 # 현재 입력된 데이터 갯수
        self._front_idx = 0
        self._rear_idx = -1

    def _empty_check(self) -> int:
        if self._size == 0:
            raise RuntimeError('Q is empty')

    def _full_check(self) -> int:
        capacity = len(self._data)
        if self._size == capacity:
            raise RuntimeError('Q is full')

    def enQ(self, value:int):
        self._full_check()

        self._rear_idx += 1
        self._rear_idx = self._rear_idx % len(self._data) # 2%4=2 ~ 4%4=0
        self._data[self._rear_idx] = value
        self._size += 1
        print('enQed:::', self._data, ', _rear_idx:::', self._rear_idx)

    def deQ(self):
        self._empty_check()

        self._front_idx += 1
        self._front_idx = self._front_idx % len(self._data)
        # 실재로 data를 삭제하는 것이 아니라
        # front포인터가 앞으로 1칸 이동하면서 동시에 사이즈를 1개 줄이는 것이 데이터가 삭제되었다고 가정되는 것입니다.
        self._size -= 1
        print('deQed:::', self._data, ', _front_idx:::', self._front_idx)

    def rear(self) -> int:
        self._empty_check()
        return self._data[self._rear_idx]

    def front(self) -> int:
        return self._data[self._front_idx]


cir_q = CircularQ(4)

cir_q.enQ(1)
print(cir_q.front(), cir_q.rear())

cir_q.enQ(2)
cir_q.enQ(3)
cir_q.enQ(4)

cir_q.deQ()
cir_q.deQ()

cir_q.enQ(5)
cir_q.enQ(6)
print(cir_q.front(), cir_q.rear())
