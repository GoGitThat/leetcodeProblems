#linktoproblem: https://leetcode.com/problems/product-of-array-except-self/

#Explanation:
#the product of all numbers except self is the same thing as saying, find the product
#to the left of self and the product to the right of self and multiply the 2
#so we can just iterate left,starting at index 0 and setting the multiplier as 1
#and simply increase the multiplier AFTER we multiply the current index by the multiplier
#and we do the same thing starting from the end calling it the right_multiplier

def productExceptSelf(nums):
    answer = [1 for _ in nums]
    left_multiplier = 1
    right_multiplier = 1
    for x in range(len(nums)):
        answer[x] *= left_multiplier
        left_multiplier *= nums[x]
    for y in range(len(nums)-1, -1, -1):
        answer[y] *= right_multiplier
        right_multiplier *= nums[y]
    return answer

#shortened version, doing it in one loop(still n^2 because you touch each item twice)
#same thing as above however, using the same index variable but negative to iterate right from
#the end of the list


def productExceptSelf2(nums):
    answer = [1 for _ in nums]
    left_multiplier = 1
    right_multiplier = 1
    for x in range(len(nums)):
        answer[x] *= left_multiplier
        answer[-1-x] *= right_multiplier
        left_multiplier *= nums[x]
        right_multiplier *= nums[-1-x]
    return answer

print(productExceptSelf([1,2,3,4])) #[24,12,8,6]
print(productExceptSelf2([1,2,3,4])) #[24,12,8,6]
