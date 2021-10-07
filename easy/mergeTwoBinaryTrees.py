#link to problem: https://leetcode.com/problems/merge-two-binary-trees/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        #if both are null or root1 is not null but root2 is
        #we dont need to merge anything into root1, so we just return
        if not root1 and not root2 or root1 and not root2:
            return root1
        #if root1 is none but root2 isn't, lets just set root1 to it
        if not root1 and root2:
            root1 = root2
        else:
            #if both are available, add the values
            if root1 and root2:
                root1.val+=root2.val
            #if left child of root1 isnt there but root2s is
            #then we simply make root1 left point to root2s left and we dont
            #to traverse down anymore
            if not root1.left and root2.left:
                root1.left = root2.left
                root2.left = None
            #same as above but for the right child
            if not root1.right and root2.right:
                root1.right = root2.right
                root2.right = None
            #if both right children available, recurse on the right child
            if root1.right and root2.right:
                self.mergeTrees(root1.right,root2.right)
            #same as above but for left child
            if root1.left and root2.left:
                self.mergeTrees(root1.left,root2.left)
        return root1

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
print(check.mergeTrees(a,f).val) #6
