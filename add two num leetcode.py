class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):  # Fixed: method name should be addTwoNumbers (not addToNumbers)
        head = ListNode(0)
        root = head
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return root.next
    # Create first list: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create second list: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Call the function
sol = Solution()
ans = sol.addTwoNumbers(l1, l2)

# Print the answer
while ans:
    print(ans.val, end=" ")
    ans = ans.next