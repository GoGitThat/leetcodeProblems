#link to problem: https://leetcode.com/problems/remove-linked-list-elements/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        prev = None
        curr = head
        while curr:
            if curr.val == val:
                if curr==head:
                    head = head.next
                if prev:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head

    def printList(self, head):
        curr = head
        while curr:
            print curr.val
            curr = curr.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(6)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

check = Solution()
newHead = check.removeElements(a, 6)
check.printList(newHead) #1,2,3,4,5
