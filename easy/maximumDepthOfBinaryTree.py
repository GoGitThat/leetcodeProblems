#link to problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root, depth = 0):
        if not root:
            return depth
        else:
            depth+=1
            return max(self.maxDepth(root.left,depth),self.maxDepth(root.right,depth))

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

check = Solution()
print(check.maxDepth(a)) #3
