#link to problem: https://leetcode.com/problems/generate-parentheses/

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    def dfs(currString, openCount, closeCount):
        #if the number of closing brackets is greater than opening, its an incorrect situation
        #or if obviously we are above the number of pairs
        if openCount > n or closeCount > n or closeCount > openCount:
            return
        if openCount == closeCount and closeCount == n:
            res.append(currString)
            
        #explore both options, adding a closing bracket and an opening bracket
        dfs(currString+"(", openCount+1, closeCount)
        dfs(currString+")", openCount, closeCount+1)
    dfs("", 0, 0)
    return res

print(generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]