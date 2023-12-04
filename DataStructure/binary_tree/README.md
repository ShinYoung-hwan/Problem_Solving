# Binary Tree

## 이진트리란?
 * 루트로부터 최대 2개의 이진트리로 이루어진 트리
 * 루트로부터 연결되어 있는 서브트리는 Left Subtree, Right Subtree로 불린다.

## 기본용어
 * Properties of Binary Tree
    - 만약 이진트리가 n개의 노드를 갖고 있다면, 그 이진트리는 n-1개의 엣지를 갖는다.
    - 만약 이진트리의 높이가 n이라면, 최저 노드 개수는 n, 최대 노드 개수는 2^n-1이다.
    - 만약 이진트리의 노드 개수가 n개라면, 최저 높이는 ceil(log2(n+1)), 최대 높이는 n이다.

 * Full Binary Tree(정이진트리)
    - leaf 노드들을 제외한 모든 노드들이 자식 노드를 갖는 이진트리를 의미한다.

 * Perfect Binary Tree(포화이진트리)
    - 높이 k인 이진트리에 모든 노드를 채운 이진트리를 의미한다.
    - 높이 k일 때 포화이진트리는 2^k-1개의 노드를 갖고 있다.

 * Complete Binary Tree(완전이진트리)
    - 마지막 레벨이 아닌 레벨의 노드는 가득 차있고, 마지막 레벨의 노드들 중에는 좌측부터 채운 이진트리를 의미한다.
    - 배열로 구현된 완전이진트리는 0부터 n-1까지 번호가 매겨진 노드에 해당하는 노드가 있는 이진 트리이다.

 * Binary Tree Traversal(이진트리탐색)
    - 트리에 있는 각각의 노드들을 탐색하는 과정
    
    * Inorder traversal: LCR(Left Center Right)
      1. Visiting a left subtree
      2. Visiting the root node
      3. visiting a right subtree
    * Preorder traversal: CLR(Center Left Right)
      1. Visiting the root node
      2. Visiting the left subtree
      3. Visiting a right subtree
    * Postorder traversal: LRC(Left Right Center)
      1. Visiting a left subtree
      2. Visiting a right subtree
      3. Visiting the root node
    * Level order traversal
      - 레벨을 내려가면서, 왼쪽 노드부터 오른쪽 노드로 이동하며 탐색하는 방법
      - 보통 큐를 통해 자식노드를 집어넣는 방식으로 구현

## 기능
 * 트리가 갖고 있는 연산들은 모두 그대로 갖고 있다.

## 사용예제
 * 디렉토리 크기 계산
 * 계산식 표현