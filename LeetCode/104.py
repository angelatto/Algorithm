"""
이진 트리의 최대 깊이 -> 즉 높이 구하기
"""
import collections
from sklearn.ensemble._hist_gradient_boosting.grower import TreeNode


def maxDepth(root:TreeNode):
    if root is None:
        return 0

    queue = collections.deque([root])
    depth = 0

    # 트리 탐색 - bfs 방식으로
    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    return depth
