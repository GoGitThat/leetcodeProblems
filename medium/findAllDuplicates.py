#link to problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/

# the solution is relatively straight forward:
#the len of the array is "n" and the range of the numbers is [1,n] inclusive
#thus each "number-1" in the array points to an index, as we traverse the array
#we simply mark the number that the index points to with a negative version of itself
#we can only mark it as negative, because we still need to preserve the number to check what itself points to
#each number we come across, if we check the number that it points to and its marked, then we add it to our return array

#i.e. [1,3,2,2,1]
#check what 1 points to, itself (1-1 = 0), mark it as negative -> [-1,3,2,2,1]
#check what 3 points to, 3 - 1 = 2, mark the number at index 2 with negative -> [-1,3,-2,2,1]
#check what -2 points to, take the absolute value, 2-1 = 1,mark the number at index 1 with negative -> [-1,-3,-2,2,1]
#check what 2 points to, 2-1 = 1,observe that the number (-3) is already negative, thus 2 repeats add it to output array
#check what -1 points to, take the absolute value, 1-1 = 0,observe that the number (-1) is already negative, thus 1 repeats add it to output array

def getRepeaters(nums):
    output = []
    for x in nums:
        if nums[abs(x)-1] < 0:
            output.append(abs(x))
        else:
            nums[abs(x)-1] *= -1
    return output

print(getRepeaters([4,3,2,7,8,2,3,1])) #[2,3]
