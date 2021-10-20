#link to problem: https://leetcode.com/problems/two-sum/

#concept:
#at each index, store the number required to fulfill the pair
#ex:2,3,4,5 target = 9 -> 7,6,5,4
#as you come across each new number, check if it exists in your map
#if exists, simply return the value of that key and the current index


def twoSum(nums, target):
    mydict = {}
    for x in range(len(nums)):
        if nums[x] in mydict:
            return [mydict[nums[x]],x]
        mydict[target-nums[x]] = x
    return []

print(twoSum([2,7,11,15],9)) #[0,1]
