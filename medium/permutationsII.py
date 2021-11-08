#link to problem: https://leetcode.com/problems/permutations-ii/

# explanation:
# same concept as "permutations.py", except notice the following:
#
# i.e [2, 1, 2, 1]
# num = 2, result -> [2]
# num = 1, result -> [1, 2], [2, 1]
# now for the repeated element 2, notice that the two results are mirrors of themselves
# see what happens when we insert 2 into each position for each array in the result:
#
# case 1: [1,2] -> [2, 1, 2], [1, 2, 2], [1, 2, 2]
# case 2: [2,1] -> [2, 2, 1], [2, 2, 1], [2, 1, 2]
#
# notice how in case 1, inserting 2 at its the position of the already existing 2 and after itself
# causes duplicate results and the same thing happens in case 2
#
# so that means we either insert for all positions up to its duplicate and all positions after itself
# but not for the position of itself or another way of putting it, we can insert for all positions up until
# it encounters itself, because for all positions after itself, it will produce duplicate results, see below:
#
# insert 2 into [1,2,3] -> [2,1,2,3], [1,2,2,3], [1,2,2,3], [1,2,3,2]
# [1,2,3] existing implies there is another array such as [1,3,2]
# if we insert 2 into [1,3,2], its possible to create [1,2,3,2] which duplicates the last item above
#
# so finally, the solution is to only insert until it encounters a duplicate and we break the position loop
# at that point and move onto the next result in the results array

def permuteUnique(nums):
    results = [[]]
    for num in nums:
        newArr = []
        for result in results:
            for position in range(len(result)+1):
                newArr.append(result[:position] + [num] + result[position:])
                if position < len(result) and result[position] == num:
                    break
        results = newArr
    return results
print(permuteUnique([1,2,3,2]))
#[[1,2,2,3],[1,2,3,2],[1,3,2,2],[2,1,2,3],[2,1,3,2],[2,2,1,3],[2,2,3,1],[2,3,1,2],[2,3,2,1],[3,1,2,2],[3,2,1,2],[3,2,2,1]]
