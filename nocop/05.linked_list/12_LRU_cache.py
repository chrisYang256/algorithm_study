"""
Least Recently Used cache

<middle>
여기서 요구하는 cache공간은 key-value 관계를 가지고 있고, chche정보를 저장하는 put(key, value) 함수, 
cache정보를 가져오는 get(value)함수가 필요합니다.
cache에 담길 수 있는 데이터의 수는 제한이 있고 이것을 3개로 제한한다면 3개 이상의 데이터가 들어왔을 때
Least Recently Used, 가장 과거에 사용(입력 or 출력)된 데이터를 삭제해줘야합니다.
1-3, 2-2, 3-9라는 데이터가 순서대로 들어왔고 이후 4-2라는 데이터가 들어왔다면 1-3을 캐시에서 삭제해줘야합니다.
만약 get(1)로 1-3이 사용된 후 4-2라는 데이터가 들어온다면 삭제되는 데이터는 2-2여야 합니다.

TC가 put(key, value): O(1), get(value): O(1)인 알고리즘은 다음과 같이 만들 수 있습니다.
put(key, value)의 구현은 get(value): O(1)를 고려해 hash table을 사용할 수 있지만 순서를 정할 수 없기 때문에
이는 array와 linked list를 생각해볼 수 있습니다.
배열은 (past)[1,2,3](recent)이고 데이터제한이 3인 해시테이블에 {1: 3, 2: 2, 3: 9}라는 데이터가 있는 경우
해시테이블에 새로운 값이 들어오면서 {1: 3}을 삭제해야 하는 경우 배열을 통해 key 1이 Least Recently Used라는 것을 바로
알 수 있지만 [ ,2,3] -> [2,3,new elem]의 과정을 거쳐야 되기 때문에 O(n)이 됩니다.

위 문제를 해결하기 위해 링크드리스트를 사용할 수 있습니다.
더미헤드를 만들어주어 (past)더미헤드->1->2->3(recent)과 해시테이블 {1: 3, 2: 2, 3: 9}가 있다면
헤드 앞에 데이터를 새로 추가하기 위해서는 O(1)이 필요하지만 가장 마지막에 추가하려면 O(n)이 필요하게 됩니다.
이 문제에서 필요로하는 조건은 가장 최근 데이터를 넣는 동작에 O(1)과 가장 과거 데이터를 제거하는 O(1)의 동작이기 때문에
이를 해결하기 위해 (past)더미헤드<->1<->2<->3<->더미테일(recent)인 doubly linked list를 이용해야 합니다.
(past)더미헤드<->1<->2<->3<->더미테일(recent)과 해시테이블 {1: 3, 2: 2, 3: 9}가 있고 1을 읽어와야 한다면
get(1)이라는 함수를 실행시킨다면 해시테이블에서 1을 찾고, 동시에 더블리리스트에서 1을 찾아 가장 최근에 사용된 쪽으로 이동하여
(past)더미헤드<->2<->3<-><->1더미테일(recent)가 되게 할 수 있습니다.
더를리리스트에서 노드를 한 번에 찾기 위해서는 해시테이블의 value에는 더블리리스트의 노드 레퍼런스가 들어가야 합니다.
그리고 노드에는 key값이 들어가는 것이 아니라 value값들을 넣어줘야 합니다.

새로운 데이터가 들어왔을 때 cache over flow가 발생하는 경우를 대비하여야 하는데
더블리리스트에서 가장 과거에 사용된 데이터를 통해 해시테이블에서 데이터를 찾아 삭제해야하기 때문에
노드에는 key값 또한 저장되어야 합니다.
"""

class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self._max_cap = capacity
        self._hash_map = {}
        self._list_head = ListNode(-1, -1)
        self._list_tail = ListNode(-1, -1)
        self._list_head.right = self._list_tail # 초기값으로 더미 헤드와 더미 테일을 엮어줌
        self._list_tail.left = self._list_head

    def _add_back(self, node: ListNode):
        tail_left = self._list_tail.left # 기존 테일노드의 왼쪽노드 불러오기

        tail_left.right = node # 기존 테일노드의 왼쪽노드의 오른쪽 노드를 새노드로 갱신, 기존테일노드왼쪽 -> 새노드
        node.left = tail_left  # 새노드 왼쪽에 헤드노드 연결, 기존테일노드왼쪽 <-> 새노드

        self._list_tail.left = node  # 테일노드의 왼쪽 노드를 새노드로 갱신, 기존테일노드왼쪽 <-> 새노드 <- 테일노드
        node.right = self._list_tail # 새노드의 오른쪽 노드를 테일노드로 연결, 기존테일노드왼쪽 <-> 새노드 <-> 테일노드

    def _remove_from_list(self, node: ListNode): # 입력된 노드의 좌우 노드를 바로 연결하여 입력된 노드 끊기
        left_node = node.left
        right_node = node.right

        left_node.right = right_node
        right_node.left = left_node

    def get(self, key: int) -> int:
        value_node = self._hash_map.get(key)
        if value_node:
            self._remove_from_list(value_node) # 삭제
            self._add_back(value_node) # 최근 이용된 값으로 갱신
            val = value_node.val
            return val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        value_node = self._hash_map.get(key)
        if value_node: # 기존 입력된 key에 새로운 value가 입력되는 경우
            value_node.val = val
            self._remove_from_list(value_node)
            self._add_back(value_node)
            return
        value_node = ListNode(key, val)
        self._hash_map[key] = value_node
        self._add_back(value_node)

        if self._max_cap < len(self._hash_map): # 메모리 초과시
            lru_node = self._list_head.right
            lru_key = lru_node.key
            self._remove_from_list(lru_node)
            self._hash_map.pop(lru_key)


lru_cache = LRUCache(4)

lru_cache.put(1, 100)
lru_cache.put(2, 200)
lru_cache.put(3, 300)
lru_cache.put(4, 400)
print('use 1:::', lru_cache.get(1))

lru_cache.put(5, 500)
print('1:::', lru_cache.get(1))
print('2:::', lru_cache.get(2)) # 1이 사용되어서 2가 가장 오래된 값이 되므로~
print('3:::', lru_cache.get(3))
print('4:::', lru_cache.get(4))
print('5:::', lru_cache.get(5))