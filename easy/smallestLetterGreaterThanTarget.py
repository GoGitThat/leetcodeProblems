#link to problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

#This is a bit of a badly worded problem, the premise is:
#return a minimum character that is larget than the target character in the sorted
#list. So if a target character is greater than the last character in the list OR
#the first character is greater than target character, just return the first character
#in the list. Otherwise you have to perform binary search.

def isBigger(letter, target):
    posString = "abcdefghijklmnopqrstuvwxyz"
    if posString.index(letter) > posString.index(target):
        return True
    if letter == "a" and target == "z":
        return True
    return False

def nextGreatestLetter(letters, target):
    start,end = 0,len(letters)-1
    minLetter = None

    if not isBigger(letters[end],target) or isBigger(letters[start],target):
        return letters[0]

    while start<= end:
        middle = (start+end)//2
        if isBigger(letters[middle], target):
            minLetter = letters[middle]
            end = middle-1
        else:
            start = middle+1

    return minLetter

print(nextGreatestLetter(["c","f","j"], "a")) #"c"
