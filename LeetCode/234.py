import collections
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #q: List = []
        # 리스트보다 Deque로 푸는것이 더 최적화된 풀이
        # 이유는 동적 배열로 구성된 리스트는 맨 앞의 값을 가져오려면 모든 값이 한 칸씩 시프팅되며 이는 O(n) 시간복잡도 발생
        # Deque 자료형은 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 O(1)이 걸린다.

        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        # 연결리스트를 데크로 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 펠린드롬 판별
        while len(q) > 1:
            # if q.pop(0) != q.pop():
            if q.popleft() != q.pop():
                return False


        return True
