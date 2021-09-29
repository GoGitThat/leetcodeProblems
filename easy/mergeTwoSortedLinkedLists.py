#link to problem: https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = tail = None

        while l1 and l2:
            if l1.val < l2.val:
                if not head:
                    head = tail = l1
                else:
                    tail.next = l1
                    tail = l1
                l1 = l1.next
            else:
                if not head:
                    head = tail = l2
                else:
                    tail.next = l2
                    tail = l2
                l2 = l2.next

        if l1:
            if tail:
                tail.next = l1
            else:
                head = tail = l1
        else:
            if tail:
                tail.next = l2
            else:
                head = tail = l2

        return head

    def printList(self, head):
        curr = head
        while curr:
            print curr.val
            curr = curr.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
g = ListNode(9)

a.next = b
b.next = c
d.next = e
e.next = f
f.next = g

check = Solution()
newHead = check.mergeTwoLists(a,d)
print(check.printList(newHead))#1,1,2,3,4,4,9
