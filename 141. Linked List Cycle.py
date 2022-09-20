class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow= head
        fast= head
        while fast is not None and fast.next is not None:
            fast= fast.next.next
            slow= slow.next
            if slow== fast:
                return True
        return False
