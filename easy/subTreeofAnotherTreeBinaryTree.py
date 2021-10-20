#link to problem: https://leetcode.com/problems/subtree-of-another-tree/
#################################################################################################################
#the following is the more intuitive solution
class Solution(object):
    #compares trees given two nodes
    def compareSubtree(self, root, subRoot):
        #if both are empty then they are equal, hence true
        if not subRoot and not root:
            return True
        #if one or the other is empty, they can never be equal, hence false
        if not root or not subRoot:
            return False
        #if the vals dont match, then obviously false
        if root.val!=subRoot.val:
            return False
        #else keep recursing, since they must match if they didnt trigger any of the earlier return calls
        return self.compareSubtree(root.left, subRoot.left) and self.compareSubtree(root.right, subRoot.right)

    #start with the actual root/subRoots
    def isSubtree(self, root, subRoot):
        #you can always find an empty node, hence true
        if not subRoot:
            return True
        #cant find any node in an empty node, hence false
        if not root:
            return False
        #if current nodes match, then recurse on subtrees
        if root.val == subRoot.val and self.compareSubtree(root,subRoot):
            return True
        #we haven't found our matching child of root that matches subRoot
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

#################################################################################################################
#solution 2: a smarter Solution
#simple premise: generate a string starting from each root and then simply check if one exists in the other
class Solution(object):
    #iterate recursively and generate a unique string (can hash the resultant string for a more robust solution)
    def generateString(self, n):
        if n:
            return "(*%$)"+str(n.val)+self.generateString(n.left)+self.generateString(n.right)+"(#^%)"
        else:
            return "@@"
    #simply check if the subroot string exists in root string
    def isSubtree(self, root, subRoot):
        return self.generateString(subRoot) in self.generateString(root)
