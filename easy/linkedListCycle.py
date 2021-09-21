#link to problem: https://leetcode.com/problems/linked-list-cycle/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

a = ListNode(3)
b = ListNode(2)
c = ListNode(2)
d = ListNode(2)

a.next = b
b.next = c
c.next = d
d.next = b
#d.next = None
#uncomment above and comment line 32 and below should be false

check = Solution()

print(check.hasCycle(a)) #true
