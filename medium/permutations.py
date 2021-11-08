#link to problem: https://leetcode.com/problems/permutations/
# explanation:
#
# i.e.
# [1, 2, 3]
# the idea is that to generate all the permutations, each number in the array will at least once
# appear at each of indices in the length of the array -> 1 should appear at i=0,i=1,i=2 -> 2 should
# appear at i=0,i=1,i=2 and so should 3
#
# the important thing to remember is, each time a number takes on a certain index, we need to save the results
# in between the iterations (like the subset problem), so we are iterating over the previous results with a new
# number and position each time
#
# [1, 2, 3]:
#
# start with empty list: [ [] ]
#
# start with num = 1
#
# for each result we have (just []), we store 1 at every position(0 since empty):
#     [1]
#
# our results is now: [1]
#
# now we are on 2:
#
# results = [ [1] ]
#
# for each result we have ([1]), we store 2 at every position possible(0 and 1):
#     [2, 1]
#     [1, 2]
#
# NOTICE: notice how for 1 we only stored it at 0 and moved onto the next num, by putting subsequent numbers at the available positions
# we automatically cover for num = 1 showing up at i=0 and i=1
#
# our results = [ [1, 2], [2, 1]]
#
# now we are on 3:
# results = [ [1, 2], [2, 1]]
#
# for each result we have ([1, 2], [2, 1]), we store 3 at every position possible(0, 1, 2):
# 3 0 [3, 2, 1]
# 3 1 [2, 3, 1]
# 3 2 [2, 1, 3]
#
# 3 0 [3, 1, 2]
# 3 1 [1, 3, 2]
# 3 2 [1, 2, 3]
#
# final result: [[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]

def permute(nums):
    results = [[]]
    for num in nums:
        newArr = []
        for result in results:
            for position in range(len(result)+1):
                newArr.append(result[:position] + [num] + result[position:])
        results = newArr
    return results

print(permute([1,2,3]))
#[[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]
