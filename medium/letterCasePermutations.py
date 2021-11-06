#link to problem: https://leetcode.com/problems/letter-case-permutation/


#this solution is as follows:
# iterate through each index in the string, if its a letter and uppercase, create a new string with
# the letter as lower case, and keep passing the string recursively until index is greater than string
# and if the string isnt in the set, simply add it

# so at each stage of the recursive call, it generates a new string (2^n combinations)
def letterCasePermutation(s, idx=0, strings = set()):
    if idx >= len(s):
        if s not in strings:
            strings.add(s)
        return
    else:
        t = None
        if s[idx].isalpha():
            if s[idx].isupper():
                t = s[:idx]+s[idx].lower()+s[idx+1:]
            else:
                t = s[:idx]+s[idx].upper()+s[idx+1:]
        if t:
            letterCasePermutation(t, idx+1, strings)
        letterCasePermutation(s, idx+1, strings)
    return list(strings)

print(letterCasePermutation("a1b2")) #['A1B2', 'a1B2', 'A1b2', 'a1b2']

# another way of doing it is to generate it through loops:
#essentially what it does is at each step, it stores the strings in result and for each
# new character, it will take the current string in result and append a lower case character and a upper case
# character to it or for numbers, it will simply append the number to it
# so at each character step, it simply generates 2 new strings for each string already existing in result aka achieving the
# same solution as the previous

def letterCasePermutation2(s):
    result=[""]
    for x in s:
        if x.isalpha():
            result = [curr + newS for curr in result for newS in (x.upper(),x.lower())]
        else:
            result = [curr+x for curr in result]
    return result
print(letterCasePermutation2("a1b2")) #['A1B2', 'a1B2', 'A1b2', 'a1b2']
