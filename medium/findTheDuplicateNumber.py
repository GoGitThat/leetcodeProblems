#link to problem: https://leetcode.com/problems/find-the-duplicate-number/

#O(N) isn't too straight forward, it is an algorithm called Floyd's cycle detection algorithmn
#the algorithm works as follows:
#think of the list as a linked list, since the length of the array is n+1 and the max number is [1,n] inclusive
#each number represents an index within the array, thus each number points to the next index

#i.e. [4,3,1,4,2]

# Graph/linked list representation:
#
#      4 -> 2 -> 1 -> 3 -> 4
#           ^              |
#           |              |
#           |______________|

#we use a slow and fast pointer, the slow pointer moves 1 through the linked list and the fast moves 2
#we iterate until slow == fast, then we reset slow back to 0
#at this point, we move slow and fast at the same pace until they are equal at which point we return the value at their indices

#Explanation:
# this works because, at the reset point (after the first collision), the fast pointer is in the cycle (see 2 -> 4 cycle above)
#and we reset slow to 0, so at one point, both pointers will be at a number next pointer points to the intersection point (2)
#this would imply that if they point to the same index in the array, then they must be the same number
#it also happens that the slow pointer will stop precisely one node before the intersection point whereas the fast pointer
#will also point to the intersection point from the end of the cycle

def FloydsAlgo(nums):
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow==fast:
            slow=0
            while True:
                if nums[slow] == nums[fast]:
                    return nums[slow]
                else:
                    slow = nums[slow]
                    fast = nums[fast]
    return 0

print(FloydsAlgo([1,3,4,2,2])) #2
print(FloydsAlgo([1,4,4,2,4])) #4
