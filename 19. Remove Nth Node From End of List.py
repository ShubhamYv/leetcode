class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        size=0
        curr= head
        while curr!= None:
            curr= curr.next
            size+=1
        if n== size:
            return head.next
        
        indexToSearch= size-n
        prev= head
        i=1
        while i< indexToSearch:
            prev= prev.next
            i+=1
        prev.next= prev.next.next
        return head
