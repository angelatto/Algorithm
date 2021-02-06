class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 연결 리스트인 rev를 구성
        while fast and fast.n_dir:
            fast = fast.n_dir.n_dir
            rev, rev.n_dir, slow = slow, rev, slow.n_dir

        if fast:
            slow = slow.n_dir

        # 펠린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.n_dir, rev.next

        return not rev
