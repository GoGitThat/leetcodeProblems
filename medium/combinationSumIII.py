#link to problem: https://leetcode.com/problems/combination-sum-iii/submissions/

##same as the other combonation sum problems with the extra condition of exactly K elements
def combinationSum3(k, n):
    
    result = []
    def dfs(currCombo, runningSum, i):
        # if the running sum is already less than 0 or we have more than k elements
        if runningSum < 0 or len(currCombo) > k:
            return
        ##we exactly have the sum and exactly k elements
        if runningSum == 0 and len(currCombo) == k:
            result.append(list(currCombo))
            return
        
        ##same backtracking, for each one dfs down from itself and higher upto 9
        ##pop it since we have explored every combo from the "choose y" scenario
        for y in range(i, 10):
            currCombo.append(y)
            dfs(currCombo, runningSum-y,y+1)
            currCombo.pop()
    dfs([], n, 1)
    return result

print(combinationSum3(3, 7)) ##[[1,2,4]]