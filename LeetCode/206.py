class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # head 바꾸기 -> 맨 끝 노드로 해드 설정
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
        
