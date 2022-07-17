#link to problem: https://leetcode.com/problems/decode-ways/

# The idea is similar to word break where you can start from the end and think of each 
# index and the letter after it as a sub problem. The base case is if the current index isn't
# 0 then its a legal char, which means that are the current + possibilities at its increasing neighbour
# however if there is a neighbour with a legal char, then you have to add the possibilities at your neighbour's
# neighbour.

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    cache = {len(s) : 1}
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            cache[i] = 0
        else:
            cache[i] = cache[i+1]
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            cache[i] += cache[i+2]
            
    return cache[0]

print(numDecodings("12")) #2