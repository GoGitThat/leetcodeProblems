#link to problem: https://leetcode.com/problems/subsets-ii/
#explained:
# the solution to this is similar to subsets 1 except we need to realize which arrays to start
# adding the new element to. Since elements can repeat, we first need to sort the number array to
# determine if the previous element matches the current one, then its becomes obvious that we need to
# start only at the new subsets that were added as a part of the last iteration, see example below:
# i.e. result = [], numbers [1,2,2]
# i = 1:
#       [] + 1 -> [1] + result -> result = [ [], [1]]
# i = 2:
#       [] + 2 -> [2], [1] + 2 -> [1, 2] + result, [ [], [1], [2], [1, 2]]
# i = 3:
        # here we see that adding "2" again to [] will result in a duplicate since our previous element
        # was also "2", same goes for adding "2" to [1], which means we need to know where the new subsets
        # that were added from i=2 begin which is at index = 2, so we simply start from index = 2 rather than 0
#       [2] + 2 -> [2, 2], [1, 2] + 2 -> [1, 2, 2] + result
#
# result = [[],[1],[1,2],[1,2,2],[2],[2,2]]

def subsetsWithDup(nums):
    result = [[]]
    nums.sort()
    for num in range(len(nums)):
        #start will represent the length from the previous iteration, if the nums dont match
        #else it will match the current length aka causing arr to start from "0"
        if num==0 or nums[num]!=nums[num-1]:
            start = len(result)
        for arr in range(len(result)-start,len(result)):
            result.append(result[arr] + [nums[num]])
    return result

print(subsetsWithDup([1,2,2])) #[[],[1],[1,2],[1,2,2],[2],[2,2]]
