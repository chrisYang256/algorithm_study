## queue

- FIFO data type

- queue의 경우 여러 자료구조의 기본이 되는 abstract data type이기 때문에 제대로 이해하는 것이 중요합니다.

- queue에는 enqueue와 dequeue가 있으며 두가지 모두 O(1)의 TS를 갖습니다.
  
  -> enqueue는 1,3,5의 데이터가 1,3,5의 순서로 입력되는 것을 말하고
  
  -> dequeue는 1,3,5의 순서대로 데이터가 출력되는 것을 말합니다.
  
  -> 데이터가 오른쪽에서 들어오면 왼쪽으로 빠지는 data structure이며 doubly linked list와 같습니다.
  
  -> 처음에 큐를 만들면 head노드와 tail노드가 생성되고 1,2,3의 데이터를 넣으면 doubly linked list가 되고
     첫 노드를 출력하면 head노드와 그다음 노드를 재연결시켜주면 되며 데이터를 삽입할 때는 tail노드쪽에서 같은 방식으로 동작하면 됩니다.
     singly list로 구현하는 방법 또한 존재합니다.