#link to problem: https://leetcode.com/problems/unique-paths/

#the idea with this problem is to realize that the last row and last column have only a single path
#so the values at those squares will be 1, otherwise the values at the squares will be the path totals
#to the right + path totals to the bottom

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    lastRow = [1] * n
    
    for row in range(m-2, -1, -1):
        currRow = [1] * n
        for col in range(n-2, -1, -1):
            currRow[col] = currRow[col+1] + lastRow[col]
        lastRow = currRow
    return lastRow[0]

print(uniquePaths(3,7)) #28