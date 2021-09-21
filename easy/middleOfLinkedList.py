#link to problem: https://leetcode.com/problems/middle-of-the-linked-list/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findMiddle(self, head):
        slow = head
        fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.val

a = ListNode(3)
b = ListNode(2)
c = ListNode(2)
d = ListNode(2)
e = ListNode(88)
f = ListNode(2)
g = ListNode(2)
h = ListNode(2)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

check = Solution()

print(check.findMiddle(a)) #88 is middle
