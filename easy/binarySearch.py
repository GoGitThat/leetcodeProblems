#link to problem: https://leetcode.com/problems/binary-search/
def search(nums, target):
    start,end = 0,len(nums)-1

    while start <= end:
        middle = (start + end)//2
        if nums[middle] == target:
            return middle
        else:
            if nums[middle] > target:
                end = middle-1
            else:
                start = middle+1
    return -1

print(search([-1,0,3,5,9,12], 9)) #4
print(search([-1,0,3,5,9,12], 85)) #-1
