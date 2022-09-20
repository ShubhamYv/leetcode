class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow= fast= head
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast= fast.next.next
        return slow
