#link to problem: https://leetcode.com/problems/path-sum/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        #if root doesnt exist and targetsum isnt 0, then its not possible
        #if root doenst exist and targetsum is 0, then its not possible
        if not root and targetSum != 0 or not root and targetSum==0:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        else:
            #else traverse down left and right paths while subtracting current
            #nodes value
            sumLeft = self.hasPathSum(root.left, targetSum-root.val)
            sumRight = self.hasPathSum(root.right,targetSum-root.val)
        return sumLeft or sumRight


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
print(check.hasPathSum(a,3)) #False
print(check.hasPathSum(a,12)) #True
print(check.hasPathSum(a,38)) #True
