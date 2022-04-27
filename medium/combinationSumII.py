#link to problem: https://leetcode.com/problems/combination-sum-ii/

def combinationSum2(candidates, target):
    results = []
    #sort to handle repeats scenario
    candidates.sort()
    def dfs(currentCombo, runningTarget, i):
        if runningTarget < 0:
            return
        if runningTarget == 0:
            results.append(list(currentCombo))
            return
        prev = 0
        for k in range(i, len(candidates)):
            if prev!=candidates[k]:
                #choose the current k and backtrack on the next one
                currentCombo.append(candidates[k])
                dfs(currentCombo, runningTarget-candidates[k], k+1)
                #IMPORTANT, this means we have already chosen k and checked out all of the combinations, pop it
                currentCombo.pop()
                ##want to skip if the previous candidate was the same(since we can have repeats and those repeats will have been explored already)
                prev = candidates[k]
    dfs([], target, 0)
    return results

print(combinationSum2([10,1,2,7,6,1,5], 8)) #[[1,1,6],[1,2,5],[1,7],[2,6]]
