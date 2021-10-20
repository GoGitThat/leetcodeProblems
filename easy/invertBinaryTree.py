#link to problem: https://leetcode.com/problems/invert-binary-tree/


#steps:
#1. hold temp pointer to left/right node
#2. set the opposite node(left/right depending on what your temp pointer points to) to point to the other node
#3. set other node to point to pointer
#4. recurse


class Solution(object):
    def invertTree(self, root):
        if root:
            temp = None
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root
