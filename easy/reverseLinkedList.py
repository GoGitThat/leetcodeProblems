#link to problem: https://leetcode.com/problems/reverse-linked-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        rev = None
        curr = head

        while curr:
            temp = curr
            curr = curr.next
            temp.next = rev
            rev = temp

        head = rev

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
newHead = check.reverseList(a)
print(check.printList(newHead))#6,5,4,3,6,2,1
