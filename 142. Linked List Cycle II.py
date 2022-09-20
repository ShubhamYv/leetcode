class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow= fast= head
        while fast and fast.next:
            slow, fast= slow.next, fast.next.next
            if slow == fast:
                break
            if not (fast and fast.next):
                return None
        while head!= slow:
            head, slow= head.next, slow.next
        return head
