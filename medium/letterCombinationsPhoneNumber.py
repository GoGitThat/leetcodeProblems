#link to problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

letterMapping = {'2' : ["a", "b", "c"],
                '3' : ["d", "e", "f"],
                '4' : ["g", "h", "i"],
                '5' : ["j", "k", "l"],
                '6' : ["m", "n", "o"],
                '7' : ["p", "q", "r", "s"],
                '8' : ["t", "u", "v"],
                '9' : ["w", "x", "y", "z"]}
def letterCombinations(digits):
    results = []
    def dfs(idx, mystr):
        #if we are past the digits length, append what we have and return
        if idx >= len(digits):
            results.append(mystr)
            return
        #if the number has corresponding letters (aka not 1 or 0)
        if digits[idx] in letterMapping:
            #for each letter just do a dfs
            for letter in letterMapping[digits[idx]]:
                dfs(idx+1, mystr+letter)
        else:
            #skip current letter and move onto next
            dfs(idx+1, mystr)
    if len(digits) > 0:
        dfs(0, "")
    return results

print(letterCombinations("23")) #["ad","ae","af","bd","be","bf","cd","ce","cf"]