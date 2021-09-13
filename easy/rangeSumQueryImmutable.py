#link to problem: https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.myl = nums
        for x in range(1,len(self.myl)):
            self.myl[x] += self.myl[x-1]


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.myl[right]
        else:
            return self.myl[right] - self.myl[left-1]


f = NumArray([-2, 0, 3, -5, 2, -1])
print(f.sumRange(0, 2)) #1
print(f.sumRange(2, 5)) #-1
print(f.sumRange(0, 5)) #-3
