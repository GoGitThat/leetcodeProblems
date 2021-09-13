#link to problem: https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    for x in range(1,len(nums)):
        if nums[x-1] > 0:
            nums[x] += nums[x-1]
    return max(nums)

print(maxSubArray([4,-1,2,1])) #6
print(maxSubArray([1])) #1
print(maxSubArray([5,4,-1,7,8])) #23
