"""
idea : 먼저 루트 노드를 찾는다.
그 다음 중위 순회에서 루트 노드의 인덱스를 찾고 이를 기준으로 트리를 재귀적으로 분리한다.
"""


def printPostorder(preorder, inorder):  # 후위 순회
    global c
    if not len(preorder):
        return

    root = preorder[0]  # 각 서브트리의 루트를 구한다.
    mid = inorder.index(root)  # 중위 순회에서 루트노드의 위치를 찾는다. 왼쪽 서브트리와 오른쪽 서브트리의 크기를 알 수 있다.

    printPostorder(preorder[1:mid+1], inorder[:mid])  # 왼쪽 서브 트리 탐색
    printPostorder(preorder[mid+1:], inorder[mid+1:])  # 오른쪽 서브 트리 탐색

    print(root, end=' ')  # 루트 노드 마지막에 출력 (후위 순휘니까)


n = int(input())
for _ in range(n):
    c = int(input())  # 노드의개수

    preorder = list(map(int, input().split()))  # 전위 순회
    inorder = list(map(int, input().split()))  # 중위 순회

    printPostorder(preorder, inorder)
    print()