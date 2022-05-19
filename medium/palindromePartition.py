#link to problem: https://leetcode.com/problems/palindrome-partitioning/
#essentially a backtracking problem:

#"aab" -> "a","a","b"
#      -> "aa", "b"

#the idea is to iterate through the string by index and maintaining a current string split list
#once you have dfs'ed down a split, pop it from the current split list and move onto the next index
#but your search space is from the split to the end of the string

def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    res = []
    #the current split
    curr = []
    def dfs(idx):
        if idx >= len(s):
            res.append(list(curr))
            return
        #check for the current range
        for i in range(idx, len(s)):
            if isPalindrome(s, idx, i):
                #if palindrome, then append and dfs from the next index
                curr.append(s[idx: i+1])
                dfs(i+1)
                #pop to backtrack and explore the next split
                curr.pop()
    dfs(0)
    return res

def isPalindrome(s, idx, i):
    while idx < i:
        if s[idx] != s[i]:
            return False
        idx+=1
        i-=1
    return True


print(partition("aab")) #[["a","a","b"],["aa","b"]]
