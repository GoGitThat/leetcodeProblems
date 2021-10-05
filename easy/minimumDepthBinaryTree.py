#link to problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root, minn = 0):
        #return if we are at leaf node
        if not root:
            return minn
        else:
            #if one child is null, we should go to the other, so we want the max value
            if not root.left or not root.right:
                minn = max(self.minDepth(root.left,minn+1),self.minDepth(root.right,minn+1))
            else:
                #else we want to get the minimum of either path
                minn = min(self.minDepth(root.left,minn+1),self.minDepth(root.right,minn+1))
        return minn

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
print(check.minDepth(a)) #2
