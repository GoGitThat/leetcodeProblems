#link to problem: https://leetcode.com/problems/combinations/

def combine(n, k):
    #hold the result
    result = []

    #current number is the current decision tree we are going down (aka chose 1 from [1,2,3,4])
    #current list is the current combination ([1,2] for example)
    def backtrack(currentNum, currentList):
        #if there are k elements we can stop
        if len(currentList) == k:
            #append a copy of the list since we will backtrack from an already selected number
            #by popping from currentlist
            result.append(list(currentList))
            return
        #since its from [1,n], any number prior to the currentNum would already cover a part of the solution set ([1,2] is the same as [2,1])
        #dont want permutations, just combinations
        for i in range(currentNum, n+1):
            #choose the current i and backtrack on the next one
            currentList.append(i)
            backtrack(i+1, currentList)
            #IMPORTANT, this means we have already chosen i and checked out all of the combinations, pop it
            currentList.pop()
            
    backtrack(1, [])
    return result

print(combine(4, 2)) #[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],] -> answer
