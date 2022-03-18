"""
<basic>
iterative_post_order_traverse는 난이도가 있는데, 이를 외울 필요는 없고 생각하는 방법만 알고 가면 됩니다.
"""

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

def iterative_pre_order_traverse(node):
    if node is None:
        return
    
    stack = []
    stack.append(node)
    while 0 < len(stack):
        pop_node = stack.pop()
        print(pop_node.val, end=' ')
        # left를 먼저 pop해야하므로 stack에 오른쪽부터 쌓고 왼쪽을 쌓아 왼쪽을 우선 pop하게 만듦
        # stack: [] -> [1] -> [] -> [3] -> [3,2] -> [3] -> [3,5] -> [3,5,4] -> [3,5] -> [3] -> [] -> [6] -> [7,6] -> [7] -> []
        if pop_node.right:
            stack.append(pop_node.right)
        if pop_node.left:
            stack.append(pop_node.left)

print(iterative_pre_order_traverse(node1))

def iterative_in_order_traverse(node):
    curr_node = node
    stack = []
    while True:
        # stack: [] -> [1] -> [1,2] -> [1,2,4] -> (4의 왼쪽 -> None) -> (elif) -> [1,2] -> (4의 오른쪽 -> None) -> (elif) -> 
        # [1] -> [1,5] -> (5의 왼쪽 -> None) -> (elif) -> (5의 오른쪽 -> None) -> [1] -> [] -> [3] -> [3,6]... ...반복
        if curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left
        
        elif 0 < len(stack):
            curr_node = stack.pop() # 현재 노드가 None이기 때문에 stack에서 뽑아옴
            print(curr_node.val, end=' ')
            curr_node = curr_node.right

        else:
            break

print(iterative_in_order_traverse(node1))

def iterative_post_order_traverse(node):
    stack = []
    # 아래 2개의 노드를 가진 노드가 current node일 때 이 current node를 pop/print할지 오른쪽을 체크할지 결정해야할 때를 위한 정보로 이용
    # current node를 pop/print할 차례인 경우::: last print node가 아래 두 노드 중 오른쪽 노드를 가리키고 있다면 오른쪽 노드가 pop/print한 후라는 의미 
    # 오른쪽 아래 node를 pop/print해야할 경우::: last print node가 아래 두 노드 중 왼쪽 노드를 가리키고 있음
    last_print_node = None
    cur_node = node
    while True:
        if cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left

        elif 0 < len(stack):
            peek_node = stack[-1] # stack[-1]가 2일때
            if peek_node.right and last_print_node != peek_node.right: # 2의 오른쪽 노드가 있고(True) + 그 오른쪽 노드가 기존에 pop된 노드인지 확인
                cur_node = peek_node.right
            else:
                print(peek_node.val, end=' ') # 오른쪽 아래가 이미 pop한 노드라면 이제 2가 프린트 될 차례
                last_print_node = stack.pop() # pop한 노드(stack[-1])를 기억

        else:
            break

print(iterative_post_order_traverse(node1))