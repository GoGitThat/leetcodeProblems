#link to question: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

def disappearedNums(nums):
    allNums = set(range(1, len(nums)+1))
    for x in nums:
        if x in allNums:
            allNums.remove(x)
    return allNums

print(disappearedNums([4,3,2,7,8,2,3,1])) #[5,6]
print(disappearedNums([1,1])) #[2]
