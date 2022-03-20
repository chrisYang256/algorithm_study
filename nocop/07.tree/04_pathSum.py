"""
<basic>
root node에서 leaf node까지의 합이 target sum이 되는 모든 path를 찾는 문제입니다.
          7
        /   \
      -2     5
      / \   / \
     3  15 8  -5
위와 같은 노드가 있고 target sum이 20이라면 7 -2 + 15 = 20, 7 + 5 + 8 = 20이 되고 [[7,-2,15], [7,5,8]]을 리턴하면 됩니다.
backtracking 챕터를 보았다면 아주 쉽게 풀 수 있는 문제입니다.
level0에 있는 root node인 노드7에서 봤을 때 노드7을 포함하여 20이 되는 path를 찾으면 되고
level1에 있는 노드-2와 노드5에서 봤을때는 자신을 포함 13이 되는 path를 찾으면 됩니다.
노드-2의 left는 3이고 합은 1이므로 해당되지 않고 right는 13이 되므로 유효한 path가 됩니다.
노드5의 left는 8이고 합은 13이르모 유효한 path가 되고 right는 -5이고 합이 0이 되므로 해당하지 않습니다.
TC는 탐색을 해야하므로 O(n), SC는 O(depth)가 필요합니다.
"""

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(7)
node2m = TreeNode(-2)
node5 = TreeNode(5)
node3 = TreeNode(3)
node15 = TreeNode(15)
node8 = TreeNode(8)
node5m = TreeNode(-5)

root.left = node2m
root.right = node5
node2m.left = node3
node2m.right = node15
node5.left = node8
node5.right = node5m

def print_tree_level(node):
    if node is None:
        return
    q = deque()
    q.append(node)
    while 0 < len(q):
        level_count = len(q)
        for _ in range(level_count):
            cur_node = q.popleft()
            print(cur_node.val, end=' ')
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        print('')

print_tree_level(root)

class PathSum:
    def get_pathes(self, root:TreeNode, target_sum:int) -> List[List[int]]:
        if root is None:
            return []

        self._ret_list = []
        self._recur_path_sum(root, target_sum, [])

        return self._ret_list

    def _recur_path_sum(self, node:TreeNode, target_sum:int, cur_list:List[int]):
        if node.left is None and node.right is None: # leaf노드까지 왔다면
            if node.val == target_sum: # leaf노드의 value가 target_sum에서 root노드/leaf노드의 상위 노드들을 뺀 값과 같다면 유효값이 됨
                cur_list.append(node.val) # 옳은 값을 cur_list에 넣고
                self._ret_list.append(cur_list.copy()) # cur_list를 옳은 값을 모으는 _ret_list에 넣음
                cur_list.pop() # 확인된 노드는 제거
            return

        new_target_sum = target_sum - node.val # 종료 조건에서 leaf값과 비교를 위해 타겟값에서 현재 노드의 값을 계속 빼줌
        print(new_target_sum)
        if node.left: # [7] -> [7,-2] -> (노드-2의 left인 노드3 종료조건 아님 확인 -> -2 pop) -> 
            cur_list.append(node.val)
            self._recur_path_sum(node.left, new_target_sum, cur_list)
            cur_list.pop()
        if node.right: # -> [7] -> (node는 아직 노드-2이므로) -> [7,-2] -> (노드-2의 right인 노드15 종료조건 맞음 -> 종료조건에서 15 pop -> 여기서 -2 pop)
            cur_list.append(node.val)
            self._recur_path_sum(node.right, new_target_sum, cur_list)
            cur_list.pop()
        return

path_sum = PathSum()

print(path_sum.get_pathes(root, 20))