#link to problem: https://leetcode.com/problems/word-break/

# the solution to this is a back to front approach where at each position we check each word from the word dictionary.
# if a word match occurs, then we mark that as true. If at letter position 0, we find a match then we check the bool
# value at the position in the "cache" array at len of the word match at 0 + 1 and that would tell us if overall the 
# word can be broken down.


def wordBreak(s, wordDict):
    #ml of the last letter would be true because that is our base case
    #if a word exactly matches the whole word then the expectation is that all letter up to last letter should match
    #depending on which index the word starts at
    #however if it matches past that, it would be false
    ml = [False] * (len(s) + 1)
    ml[len(s)] = True
    
    #iterate backwards at each index
    for letter in range(len(s)-1, -1,-1):
        for word in wordDict:
            #if the word length fits and the word matches, mark that position based on current index + len of curr word
            if letter + len(word) <= len(s) and s[letter:letter+len(word)] == word:
                ml[letter] = ml[letter + len(word)]
            ##we've already found a match, we can move onto the next index
            if ml[letter]:
                break
    return ml[0]

print(wordBreak("leetcode", ["greek", "leet", "brode"])) #false
print(wordBreak("leetcode", ["greek", "leet", "code"])) #true