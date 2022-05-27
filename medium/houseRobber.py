#link to problem: https://leetcode.com/problems/house-robber/


#link to problem: https://leetcode.com/problems/house-robber/



# the premise of this problem is pretty straightforward
# say we have a list of numbers [1.....n]

# so at the begining the total is 0:

# now we have two choices, add the first number or skip it, its obvious add the first number since that total is greater than 0

# assume we had a list of totals at each index as we went through the array, it would look like -> [0 -> empty list total, 0 + list[0]]

# then we just take the max at each step, we either add the current number and the total prior to the previous element or we take the previous element

# at each number we have to make a decision, do we include this number or do I skip and use the previous running total


def rob(nums):
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

print(rob([1,2,3,1])) #4

