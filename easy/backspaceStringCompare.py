#link to problem: https://leetcode.com/problems/backspace-string-compare/

#naive solution:
#produce an array from each input string
#if letter add it to array, if backspace remove latest from array (aka stack)
#compare outputs of both strings (O(m+n) space and time complexity)
def produceString(s):
    arr = []
    for x in s:
        if x!="#":
            arr.append(x)
        else:
            if len(arr) >= 1:
                arr.pop()
    return arr
def backspaceCompare(s, t):
    return produceString(s) == produceString(t)

print(backspaceCompare("ab#c","ad#c")) #true

#better solution:

#the idea is to find all the valid chars (those that dont get deleted by "#")
#then while the chars still exist in each string, get the next valid char in each
#if they dont match, return false

#To get valid chars do the following:
#iterate through the input string from the end, if you come across "#", that means
#we have to skip the next valid char since it will be deleted by the "#" we came across
#so while the count of "#" is not 0, keep finding a character, once skipCount is 0
#the next character is valid, thus return it

def getValidChar(s, idx):
    t = idx
    skipCount = 0
    while t >= 0:
        if s[t]=="#":
            skipCount+=1
        else:
            if skipCount==0:
                return s[t],t
            else:
                skipCount-=1
        t-=1
    return None,t

def backspaceCompare(s, t):
    s_len = len(s)-1
    t_len = len(t)-1
    while s_len >= 0 or t_len >= 0:
        s_char,s_len = getValidChar(s, s_len)
        t_char,t_len = getValidChar(t, t_len)
        if s_char!=t_char:
            return False
        s_len-=1
        t_len-=1
    return True

print(backspaceCompare("ab#c","ad#c")) #true
