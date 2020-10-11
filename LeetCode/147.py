class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 팔요한 경우에만 cur 포인터가 되돌아가도록 처리한다.
            # 이것에 따라 성능이 10배 이상 차이난다.
            if head and cur.val > head.val:
                cur = parent
        return parent.next
