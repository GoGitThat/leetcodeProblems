#link to problem: https://leetcode.com/problems/target-sum/

#the idea is to perform dfs and store the index, runningTotal at that index taht leads to the target
#for each parent call, if the total is found in the cache, return it

def findTargetSumWays(nums, target):
    memo = {}
    def dfs(idx, runningTotal):
        if idx == len(nums):
            if runningTotal == target:
                return 1
            else:
                return 0
        if (idx, runningTotal) in memo:
            return memo[(idx, runningTotal)]
        memo[(idx, runningTotal)] = dfs(idx+1, runningTotal-nums[idx]) + dfs(idx+1, runningTotal+nums[idx])
        return memo[(idx, runningTotal)]
    return dfs(0, 0)

print(findTargetSumWays([1,1,1,1,1], 3)) #5