- Tree / binary tree: 

    • 나무와 같은 구조를 가진 linked list 비슷한 자료구조입니다.

    • tree에는 root node가 있고 children node들을 가지고 있습니다.
       각각의 노드들은 여러 칠드런 노드를 가지 수도 있고 하나의 child 노드를 가질 수도 있습니다.
       만약 칠드런의 갯수가 2개로 제한된다면 이를 binery tree라고 부르며 바이너리 트리에는 여러 종류가 있습니다.
       full binary tree: 각각의 노드가 2개의 차일드만 가지고 있거나 아무것도 가지고 있지 않음.
       complete binary tree: 노드의 마지막 레벨이 왼쪽으로 치우쳐 정렬되어 있음.
       perfect binary tree: 모든 노드들이 2개의 노드를 가지고 있고 leaf의 level이 같은 것을 의미.

<br/>

- Tree traverse(Tree의 순환)

          N
        /   \
       L     R

    • pre order traverse: 'N' -> L -> R 로 노드의 순서가 됨

    • in order traverse: L -> 'N' -> R

    • post order traverse: L -> R -> 'N'

<br/>

          1
        /   \
       2     3
      / \   / \
     4   5 6   7

    • pre order traverse: 1,2,4,5,3,6,7

    • in order traverse: 4,2,5,1,6,3,7

    • post order traverse: 4,5,2,6,7,3,1

<br/>

- LCA: 공통 조상 문제

<br/>

- BST(Binery search Tree)

<br/>

- Trie(문자열 관리 데이터타입)

<br/>

- 10+ problems
