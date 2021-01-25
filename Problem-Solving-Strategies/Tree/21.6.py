"""
트리에서 가장 긴 경로 찾기
- max (가장 긴 루트-리프 경로의 길이, 가장 긴 리프-리프 경로의 길)
- 여기서 가장 긴 루트-리프 경로의 길이는 트리의 높이와 같다.
- 가장 긴 리프-리프 경로의 길이는 각 서브트리마다 재귀적으로 구해야 한다.

1. 노드 구현
2. 트리 생성
3. 트리 탐색 (가장 긴 경로 찾기)
"""
import math


class Node:  # 노드를 구현
    def __init__(self, x, y, r):
        print('---2---')

        self.x = x
        self.y = y
        self.r = r
        self.child = []

    def isIn(self, node):
        distance = math.sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)  # 두 원의 거리

        if distance < node.y:
            return True
        else:
            return False

    def addChild(self, node):
        self.child.append(node)


class Tree:  # 트리 생성
    def __init__(self):
        self.root = None
        self.distance = 0

    def add(self, node):
        if self.root:
            self.add_rec(self.root, node)
        else:
            self.root = node

    def add_rec(self, root, node):
        for child in root.child:
            if node.isIn(child):
                self.add_rec(child, node)

        root.addChild(node)

    def maxDistance(self):
        self.maxDepth(self.root)

    def maxDepth(self, node):
        # node를 root로 하는 트리안에서 최대 거리 구하기
        if not node.child:
            return 1
        depths = []
        maxDepth = 1
        for child in node.child:
            sub_depth = self.maxDepth(child)
            maxDepth = max(maxDepth, sub_depth + 1)
            depths.append(sub_depth)

        if len(depths) > 1:
            depths = sorted(depths, reverse=True)
            self.distance = max(self.distance, depths[0] + depths[1])
        else:
            self.distance = max(self.distance, depths[0])

        return maxDepth


# __main__
tc = int(input())
for _ in range(tc):  # 하나의 테스트케이스 실행
    N = int(input())  # 노드의 개수
    fortree = []
    for _ in range(N):
        x, y, r = list(map(int, input().split()))
        fortree.append((x, y, r))

    fortree = sorted(fortree, key=lambda x: -x[2])  # 반지름이 큰 순으로 정렬

    # 실제 트리 생성 - 위에서 fortree 리스트로 만들기
    tree = Tree()
    for x, y, r in fortree:
        tree.add(Node(x, y, r))

    tree.maxDistance()
    print(tree.distance)  # 답
