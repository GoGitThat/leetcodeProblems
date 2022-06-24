#link to problem: https://leetcode.com/problems/longest-increasing-subsequence/

# the idea is to begin backwards since the count at the last number will be one
# the count at the previous to the last will be 1 if the last number was smaller (aka non increasing)
# else it would be 1 + itself, so on and so forth. Hence we loop backwards and then internally loop forwards
# for every number that comes before the current backwards number and at each point it will either be the max
# between "1" or the largest consecutive at any number that comes after current if they are larger

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cache = [1] * len(nums)
    
    for x in range(len(nums)-1,-1,-1):
        for y in range(x+1, len(nums)):
            if nums[x] < nums[y]:
                cache[x] = max(cache[x], 1 + cache[y])
    return max(cache)

print(lengthOfLIS([10,9,2,5,3,7,101,18])) #4