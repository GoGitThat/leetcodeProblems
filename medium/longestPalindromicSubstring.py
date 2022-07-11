#link to problem: https://leetcode.com/problems/longest-palindromic-substring/


# this one can be resolved if you think of how a palindrome works. It looks the same if you flip the word.
# in this way you can check for a palindrome either from the outside, comparing letters going inwards or vice versa
# so if we think of each letter as being the "center" then we simply need to check for the longest palindrome assuming
# each letter is the center and comparing letters to the left and right keeping in mind the case where the number of 
# letters is odd, in which case the left and right pointers start being an index apart.

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    retStr = ""
    maxLen = 0
    
    for i in range(len(s)):
        l,r = i, i
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l + 1 > maxLen:
                maxLen = r-l+1
                retStr = s[l:r+1]
            l-=1
            r+=1
        
        l,r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l + 1 > maxLen:
                maxLen = r-l+1
                retStr = s[l:r+1]
            l-=1
            r+=1
            
    return retStr

print(longestPalindrome("babad")) #bab