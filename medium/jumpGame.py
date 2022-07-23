#link to problem: https://leetcode.com/problems/jump-game/

#the idea with this problem is to realize that the index + number at that index determines how far you can get in the array
#so at each point in the array you simply have to keep updating, checking how far you can jump and if it is greater than
#the difference between the size of the array and the current index, then simply update it to the current index
#if by the item you get to the first index, the jump distance required is 0, then you know you have more than enough jump distance
#to get to the last index

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    last = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i+nums[i] >= last:
            last = i
    return last==0


print(canJump([2,3,1,1,4])) #true