#link to problem: https://leetcode.com/problems/squares-of-a-sorted-array/
def sortedSquares(nums):
    #if less than 2 items, simply square and return
    if len(nums) < 2:
        return [x**2 for x in nums]
    #init a new list with same len as the original one
    newL = [None] * len(nums)
    #hold indices from start/end of original list
    #hold index to the largest open index in the new list
    i = len(nums)-1
    j = 0
    idx = len(nums)-1
    #while the index of the beginning pointer < ending pointer
    #opposite implies we have already processed everything
    while j <= i:
        #take the larger value, square it and put it at the max index in the new array
        if abs(nums[j]) > abs(nums[i]):
            newL[idx] = nums[j] ** 2
            j+=1
        else:
            newL[idx] = nums[i] ** 2
            i-=1
        idx-=1
    return newL

print(sortedSquares([-4,-1,0,3,10])) #[0,1,9,16,100]
