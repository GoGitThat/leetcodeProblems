#link to problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q, tn = None):
        if not root:
            return tn
        else:
            myMin = min(p.val,q.val)
            myMax = max(p.val,q.val)
            if root.val >= myMin and root.val <= myMax:
                tn = root
            if root.val > myMax:
                tn = self.lowestCommonAncestor(root.left, p, q, tn)
            if root.val < myMin:
                tn = self.lowestCommonAncestor(root.right, p, q, tn)
        return tn

a = TreeNode(7)
b = TreeNode(3)
c = TreeNode(9)
d = TreeNode(15)
e = TreeNode(20)
a.left = b
a.right = c
c.right = d
d.right = e

check = Solution()
print(check.lowestCommonAncestor(a, b, d).val) #7
