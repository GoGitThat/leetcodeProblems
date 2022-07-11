#link to problem: https://leetcode.com/problems/combination-sum-iv/

# the idea of this is a bottom up approach. For the target number, we already have a list of numbers that we know are reachable
# because they are already in the list, so the question then becomes how many different ways can you reach the difference between 
# the target and the numbers in the list. So say we have a target of 4 and the array is 1,2,3. We know 1,2,3 is reachable so say we chose 
# 1 as one of the numbers then the remainder is 3, so then the question would be how many ways can we reach 3 and then we repeat the process 
# for each number in the list and so the total of those permutations would be the answer.

def combinationSum4(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    cache = {}
    #an empty list is reachable only one way, no items, base case
    cache[0] = 1
    
    #bounds are for positive numbers
    for targ in range(1, target+1):
        #default to 0
        cache[targ] = 0
        for num in nums:
            #if the sub problem is in the cache, add it
            if (targ-num) in cache:
                cache[targ] += cache[targ-num]
    return cache[target]

print(combinationSum4([1,2,3], 4)) #7