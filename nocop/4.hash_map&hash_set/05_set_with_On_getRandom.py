"""
<middle>
TC O(1)을 갖는 insert, remove, getRandom을 impelmentation하라는 복합 데이터 스트럭쳐를 만드는 문제입니다.
3, 5, 7, 5가 insert되면 set에는 3, 5, 7만 들어가는데 이는 중복제거 기능이 있어야 한다는 의미입니다.
2, 7이 delete되면 set에서 7은 삭제되고 2는 없기 때문에 별다른 동작을 하지 않아도 됩니다.
그리고 getRandom은 여러개의 데이터 중에서 랜덤한 값을 가져와야하고 세가지 동작 모두 O(1)으로 구현해야 합니다.

array와 hash_map을 통해 다음과 같이 각각 O(1)로 구현할 수 있습니다.
insert는 입력되는 값을 hash map에서 찾고 없는 경우에만 array에 입력합니다.
getRandom은 사용하는 언어의 기능으로 array에서 추출합니다.
remove의 경우 hash map에서 O(1)으로 값을 찾을 수 있지만 arr은 좌에서 우로 순회하면 O(n)을 갖습니다.
그러므로 insert할 때 array에 입력되는 값의 idx를 hash map에 입력해둘 경우
hash map에서 O(1)으로 찾음/idx를 구해 array에서 삭제할 값을 O(1)로 구할 수 있습니다.
하지만 삭제할 값이 요소 사이에 있는 경우 그대로 삭제하면 array에 빈공간이 생기기 때문에
마지막 숫자를 해당 위치에 복사하고 마지막 숫자는 지워주면 삭제와 빈공간문제가 해결됩니다.
hash map에서는 해당 값을 삭제하고 array에서 이동한 마지막 숫자의 idx를 가져와 hash map에서도 업데이트해 주면 됩니다.

(hash set은 hash map에서 value가 없는 상태나 key와 value가 같은 값을 가진 데이터구조)
"""

import random

class RandomReturn:
  def __init__(self):
    self._table = {}
    self._arry = [] # hash_set이 되는 부분

  def insert(self, val: int) -> bool:
    idx = self._table.get(val)
    if idx is not None: # table에 값이 이미 존재하는 경우 insert되지 않음. array 순회 필요 없음
      return False

    idx = len(self._arry) # 배열에 값 삽입 전 idx값을 구함. 삽입부터 할 경우 len(self._arry)-1을 하면 됨
    self._arry.append(val) # 배열에 삽입 
    self._table[val] = idx # 배열의 idx를 value로 지정하여 O(1)이 가능
    return True

  def remove(self, val: int) -> bool:
    idx = self._table.get(val) # table의 key로 idx 추출
    if idx is None:
      return False

    last_val = self._arry[-1]
    self._arry[idx] = last_val # 삭제할 idx에 배열의 마지막 값을 넣으므로써 의도대로 해당 숫자는 삭제
    self._arry.pop() # 배열에 공백이 생기지 않으면서 삭제된 값 이외의 값(arr[-1])은 보존됨
    self._table[last_val] = idx # 배열에서 빠진 값의 자리로 간 값(last_val)과 table의 값이 똑같은 idx를 갖도록 key의 value(idx)를 수정
    self._table.pop(val) # O(1)
    
    return True
    
  def getRandom(self) -> int:
    return random.choice(self._arry)

randomReturn = RandomReturn()

print(randomReturn.insert(3), end=' ')
print(randomReturn.insert(3), end=' ')
print(randomReturn.insert(5), end=' ')
print(randomReturn.insert(7), end=' ')
print(randomReturn.getRandom(), end=' ')
print(randomReturn.remove(3), end=' ')
print(randomReturn.remove(3), end=' ')
print(randomReturn.getRandom(), end=' ')