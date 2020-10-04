class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 연결리스트를 리스트로 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 펠린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False


        return True


    print(isPalindrome(1 -> 2))
