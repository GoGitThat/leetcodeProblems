#link to problem: https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):
    result = []
    def dfs(idx, comboList, runningSum):
        #if the target matches, append to the result list
        if runningSum == target:
            result.append(list(comboList))
            return
        #if we are higher than the target or are out of candidates, return
        if runningSum > target or idx >= len(candidates):
            return
        #else we still have room, so append the current candidate and dfs down
        comboList.append(candidates[idx])
        dfs(idx, comboList, runningSum + candidates[idx])
        ##we've already explored the current candidate
        comboList.pop()
        ##move onto the next candidate
        dfs(idx+1, comboList, runningSum)
    dfs(0,[],0)
    return result

print(combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]