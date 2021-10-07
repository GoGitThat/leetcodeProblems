#link to problem: https://leetcode.com/problems/same-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # if one is null and the other isnt, false
        if not p and q or p and not q:
            return False
        if not p and not q:
            return True
        if p.val!=q.val:
            return False
        else:
            isSameLeft = self.isSameTree(p.left,q.left)
            isSameRight = self.isSameTree(p.right,q.right)
        return isSameLeft and isSameRight

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

f = TreeNode(3)
g = TreeNode(9)
h = TreeNode(20)
i = TreeNode(15)
j = TreeNode(7)
f.left = g
f.right = h
h.left = i
h.right = j

check = Solution()
print(check.isSameTree(a,f)) #True
