class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result=ListNode(0)
        head=result
        while list1 and list2:
            if list1.val<=list2.val:
              head.next=list1
              list1=list1.next
            else:
              head.next=list2
              list2=list2.next
            head=head.next
        if list1:
            head.next=list1
        if list2:
            head.next=list2
        return result.next
l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(44)

# Create second list: 5 -> 6 -> 4
l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(994)

# Call the function
sol = Solution()
ans = sol.mergeTwoLists(l1, l2)

# Print the answer
while ans:
    print(ans.val, end=" ")
    ans = ans.next