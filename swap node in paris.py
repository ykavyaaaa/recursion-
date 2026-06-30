class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
         """
        dummy = ListNode(0, head)
        prev,curr=dummy,head
        while curr and curr.next:
            nextpair=curr.next.next
            second=curr.next
            second.next=curr
            curr.next=nextpair
            prev.next=second
            prev=curr
            curr=nextpair
        return dummy.next
def printList(head):
    while head:
     print(head.val, end=" -> " if head.next else "")
    head = head.next
    print()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
head = sol.swapPairs(head)
printList(head) 