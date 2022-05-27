#link to problem: https://leetcode.com/problems/house-robber-ii/

# this is a very similar problem to house robber 1 with the difference that you cant use the
# first and last element since they are considered to be adjacent, so the solution is simply to 
# return the max of house robber 1 solution on the array not including the first element and house robber 1
# not including the last element


def robI(nums):
    #prev_2 is the running max total
    # prev is the element prior to prev_2 
    prev, prev_2 = 0, 0
    for x in nums:
        #if we add current number x to the prev vs the second last element with respect to x
        curr = max(prev + x, prev_2)
        #update to the second last
        prev = prev_2
        #will hold the running max
        prev_2 = curr
    return prev_2

def robII(nums):
    if len(nums) == 1:
        return nums[0]
    
    return max(robI(nums[1:]), robI(nums[:-1]))

print(robII([2,3,2])) #3