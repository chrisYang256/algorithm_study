"""
직접 스택 데이터 컨테이너를 만드는 문제입니다.
스택 관련 명령어 push, pop, top에 가장 큰 값을 리턴하는 max명령어를 만들어야 합니다.

max명령어가 불려질 때 배열의 값들을 하나씩 체크하고 max값을 찾는 경우 O(n)이 됩니다.
binary search는 정렬이 필요하여 O(log n)이 되고, heap은 O(n)의 space complexity가 더 필요하게 됩니다.

아래 솔루션은 스택을 두개 만들어 하나는 일반적인 스택을, 하나는 max를 위한 스택을 만들어줍니다.
스택이 쌓일 때 Max전용 스택에는 들어온 값들 중 가장 큰 값으로 치환하여 쌓는 방법입니다.
가장 큰 값을 스택 맨 위에서 바로 가져올 수 있으므로 O(1)의 시간복잡도를, 스택을 하나 더 쌓음으로 공간복잡도 O(n)가 추가됩니다.

또다른 솔루션1: 만약 max스택에는 기존의 max값보다 작은 수가 들어오는 경우 스택을 쌓지 않고, 스택을 삭제할 때에는
삭제된 값이 max값보다 작은 경우 삭제하지 않아도 목적에 부합하게 됩니다.
또다른 솔루션2: max스택에 똑같은 가장 큰 값이 계속해서 들어오는 것을 방지하기 위해 같은 숫자가 들어오는 경우 카운팅 횟수만 늘려주는 
조금 더 복잡한 data structure가 들어가는 방법도 있습니다.)
"""

class MaxStack:
    def __init__(self): # 문법설명: class의 정보를 유지하기 위해 사용
        self._stack = []
        self._max_stack = []

    def push(self, v):
        if len(self._stack) == 0:
            self._stack.append(v)
            self._max_stack.append(v)
            return
        
        max_num = self._max_stack[-1]
        if v < max_num:
            self._stack.append(v)
            self._max_stack.append(max_num)
        else:
            self._stack.append(v)
            self._max_stack.append(v)

    def pop(self):
        if len(self._stack) != 0:
            self._stack.pop()
            self._max_stack.pop()

    def top(self):
        return self._stack[-1]

    def max(self):
        return self._max_stack[-1]

MS = MaxStack()
MS.push(5)
print(MS.max())
MS.push(10)
print(MS.max())
MS.push(20)
print(MS.max())
MS.pop()
MS.pop()
print(MS.max())