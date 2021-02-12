class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 연결리스트 -> 파이썬 리스트
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.n_dir

        # 정렬
        lst.sort()

        #파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.n_dir
        return head
