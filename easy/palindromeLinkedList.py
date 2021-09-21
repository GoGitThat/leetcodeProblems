#link to problem: https://leetcode.com/problems/palindrome-linked-list/

#steps to solve:
#get to the center of the list
#need to traverse in reverse while traversing forward from center
#compare nodes and return true if they match continuously

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        #reference to head that goes in reverse
        newHead = None

        #find center of the list
        while fast and fast.next:
            #hold reference to middle node
            temp = slow
            #move the middle node
            slow = slow.next
            fast = fast.next.next
            #update newHead
            temp.next = newHead
            newHead = temp

        #fast not null implies odd number of nodes in list
        #move slow one forward
        if fast:
            slow = slow.next

        while newHead:
            if newHead.val!=slow.val:
                return False
            newHead = newHead.next
            slow = slow.next

        return True

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(3)
f = ListNode(2)
g = ListNode(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

check = Solution()
print(check.isPalindrome(a))
