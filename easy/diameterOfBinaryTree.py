#link to problem: https://leetcode.com/problems/diameter-of-binary-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        #set up the class variable
        self.depth = 0
        #start from the root of tree
        self.getDepth(root)
        return self.depth

    def getDepth(self, node):
        if not node:
            return 0
        else:
            #get depth from left and right branches
            left = self.getDepth(node.left)
            right = self.getDepth(node.right)
            #update the highest depth we've found so far
            self.depth = max(self.depth, left+right)
            #return whichever is the max + 1 from connection to parent
            return max(left,right)+1

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
print(check.diameterOfBinaryTree(a)) #3
