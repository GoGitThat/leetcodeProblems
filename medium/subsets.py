#link to problem: https://leetcode.com/problems/subsets/

# the solution is as follows:
# start with the empty set in the result "[]" for each number we encounter, since its guaranteed
# to be unique, we can simply iterate through the existing sets in result and append our number to it
# then we append all of these to result.
# i.e. result = [], numbers [1,2,3]
# i = 1:
#       [] + 1 -> [1] + result -> result = [ [], [1]]
# i = 2:
#       [] + 2 -> [2], [1] + 2 -> [1, 2] + result, [ [], [1], [2], [1, 2]]
# i = 3:
#       [] + 3 -> [3], [1] + 3 -> [1, 3], [2] + 3 -> [2, 3], [1, 2] + 3 -> [1, 2, 3] + result
#
# result = [ [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def subsets(nums):
    result = [[]]
    for n in nums:
        result+=[x+[n] for x in result]
    return result

print(subsets([1,2,3])) #[ [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
