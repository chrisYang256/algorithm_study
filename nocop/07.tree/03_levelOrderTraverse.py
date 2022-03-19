"""
<basic>
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
위와 같은 트리가 있는 경우 level 0은 1, 1은 2,3, 2는 4,5,6,7,이며 이를 각 level의 
좌에서 우로, 위에서 아래로 순서대로 1,2,3,4,5,6,7를 출력하는 문제입니다.

solution1:::
이 자체를 FIFO를 가지는 Q로 볼 수 있습니다.
Q에 노드1을 넣고 deQ를 하고 프린트를 하고 노드1에 대한 left, right인 노드2, 노드3을 enQ해줍니다.
이어서 노드 2를 deQ하고 프린트한 후 노드2에 대한 left, right인 노드4, 노드5를 enQ해줍니다.
노드3을 deQ / 프린트하고 노드3에 대한 left, right인 노드6, 노드7을 enQ해주면 [4,5,6,7]이 됩니다.
이제 Q에 남아있는  left, right가 없는 [4,5,6,7]를 deQ해주면 1,2,3,4,5,6,7이 출력되게 됩니다.

solution2:::
각 레벨마다 몇 개의 node가 있는지 카운트하고 그 카운트만큼 deQ하고 enQ하는 방식입니다.
level0의 노드1을 enQ하고 count를 level0의 사이즈인 1로 업데이트해준 후 노드가 없는 것을 확인하고 노드1을 deQ / 프린트해줍니다.
level1의 노드2, 노드3을 enQ하고 카운트를 level2의 사이즈인 2로 업데이트합니다.
그리고 노드2를 deQ하면서 노드1 다음 라인으로 프린트해주고 그 left와 right인 노드4, 노드5를 enQ해줍니다.
이제 노드3을 deQ / 프린트하면 count만큼 deQ가 된 것입니다.
노드3의 left와 right인 노드6, 노드7을 enQ해주면 더이상 들어올 노드가 없기 때문에 
카운트를 level2의 사이즈인 4로 업데이트한 후 level2의 노드들을 level1의 노드들인 2,3의 다음 라인으로 프린트해줍니다.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

def tree_level_print1(node):
    if node is None:
        return
    
    q = deque()
    q.append(node)

    while 0 < len(q):
        cur_node = q.popleft()
        print(cur_node.val, end=' ')
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

print(tree_level_print1(node1))

def tree_level_print2(node):
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

tree_level_print2(node1)