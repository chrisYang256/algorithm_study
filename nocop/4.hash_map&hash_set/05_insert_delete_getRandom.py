"""
<middle>
TC O(1)을 갖는 random Return을 지원하는 hash Set을 구현하는 문제입니다.
"""

import random
from typing import List  

class RandomReturn:
  def __init__(self):
    self._table = {}
    self._arry = []

  def insert(self, val: int) -> bool:
    idx = self._table.get(val)
    if idx is not None:
      return False

    idx = len(self._arry)
    self._arry.append(val)        
    self._table[val] = idx
    return True

  def remove(self, val: int) -> bool:
    idx = self._table.get(val)
    if idx is None:
      return False

    last_val = self._arry[-1]
    self._arry[idx] = last_val
    self._table[last_val] = idx
    self._arry.pop()
    self._table.pop(val)
    
    return True
    
  def getRandom(self) -> int:
    return random.choice(self._arry)

randomReturn = RandomReturn()

print(randomReturn.insert(3), end=' ')
print(randomReturn.insert(5), end=' ')
print(randomReturn.insert(7), end=' ')
print(randomReturn.getRandom(), end=' ')