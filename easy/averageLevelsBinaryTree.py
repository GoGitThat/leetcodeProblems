#link to problem: https://leetcode.com/problems/average-of-levels-in-binary-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        #Create Queue for Breadth First Search
        myQ = [root]
        #will hold sums for each level
        sums = []

        while myQ:
            #for the current level, get number of nodes to iterate
            #sum variable to hold totals for current level
            numNodes,mySum = len(myQ),0
            for x in range(numNodes):
                #FIFO, get first node from Queue
                tempNode = myQ.pop(0)
                #add sum
                mySum+=tempNode.val
                #if left or right not null, add to queue(represents next level)
                if tempNode.left:
                    myQ.append(tempNode.left)
                if tempNode.right:
                    myQ.append(tempNode.right)
            #after processing each level, get average and add to our array
            sums.append(mySum/float(numNodes))
        return sums

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
print(check.averageOfLevels(a)) #[3,14.5,11]
