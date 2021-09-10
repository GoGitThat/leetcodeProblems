#link to problem: https://leetcode.com/problems/single-number/

def findSingleNumber(nums):
    runningSum=0
    for x in set(nums):
        runningSum+=x*2
    return runningSum - sum(nums)

print(findSingleNumber([2,2,1])) #1
print(findSingleNumber([4,1,2,1,2])) #4
print(findSingleNumber([1])) #1
