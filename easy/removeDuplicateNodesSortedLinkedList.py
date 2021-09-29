#link to problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        prev = head
        temp = None
        curr = head

        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = curr
            else:
                temp = curr
                curr = curr.next
                temp.next = None

        return head

    def printList(self, head):
        curr = head
        while curr:
            print curr.val
            curr = curr.next

a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(2)
e = ListNode(2)
f = ListNode(3)
g = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

check = Solution()
newHead = check.deleteDuplicates(a)
check.printList(newHead) #1,2,3,4
