#link to problem: https://leetcode.com/problems/longest-consecutive-sequence/

# the solution is as follows:
# store the numbers in a set(takes O(N)), makes it O(1) to check if consecutive numbers are present
# then loop through the set, for each number check if a less consecutive number is found in the set, if not
# start counting until we hit a non-consecutive number, at that point compare our current max with the stored max
# and update it
#
# if a less consecutive number exists, then eventually we will count from there, so the solution ends up covering all
# the numbers eventually

def longestConsecutive(nums):
    nums = set(nums)
    maxLen = 0
    for num in nums:
        if num-1 not in nums:
            nextNum = num+1
            counter = 1
            while nextNum in nums:
                counter+=1
                nextNum+=1
            maxLen = max(counter, maxLen)
    return maxLen

print(longestConsecutive([100,4,200,1,3,2])) #4
