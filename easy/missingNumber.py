#link to problem: https://leetcode.com/problems/missing-number/

def missingNumber(nums):
    # x = sum(range(0,len(nums)+1))
    # return x - sum(nums)
    return ((len(nums) * (len(nums)+1))/2) - sum(nums)

print(missingNumber([3,0,1])) #2
print(missingNumber([0,1])) #2
print(missingNumber([9,6,4,2,3,5,7,0,1])) #8
print(missingNumber([0])) #1
