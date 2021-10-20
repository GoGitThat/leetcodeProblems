import math
#link to problem: https://leetcode.com/problems/majority-element/

#very naive solution:
#store a key for every number we come across, and increment counter for it
#return key with max counter
def majorityElement1(nums):
    mapp = {}
    for x in nums:
        if x in mapp:
            mapp[x]+=1
        else:
            mapp[x]=1
    return max(mapp, key=mapp.get)


print(majorityElement1([1,1,1,1,1,1,8])) #1


#second way, a bit less obvious:
# since the majority element must show up more than the floor(n/2), when sorted
# the middle index should hold the majority element

##QUICKSORT------
def partition(arr, start, end):
    #will hold index of an element that is greater than our pivot (arr[end])
    #aka it has to track the number of elements that are smaller than our pivot
    #since the number_of_elements = our index of where the pivot should be, we can
    #just use it as our index at the end
    j = start
    for x in range(start,end):
        if arr[x] < arr[end]:
            arr[x],arr[j]=arr[j],arr[x]
            j+=1
    #here we swap the pivot with our element at j which should be just bigger than pivot
    arr[j],arr[end]=arr[end],arr[j]
    return j

def quickSort(arr, start, end):
    #if we are on the same index, it's all sorted
    if start >= end:
        return
    else:
        #split it and sort prior to pivot and post pivot
        part = partition(arr, start, end)
        quickSort(arr, start, part-1)
        quickSort(arr, part+1, end)

def majorityElement2(nums):
    quickSort(nums, 0, len(nums)-1)
    return nums[int(math.ceil(len(nums)/2.0))]

print(majorityElement2([8,8,8,8,1,1,1])) #8

#third way and the least obvious: Boyer-Moore algorithmn
#assume the first element is the majority, if the next element does not match
#the current majority element, detract 1 from the counter
#if counter is 0, then we set the current element as the new majority

##this works because:
#1. if we come across a pair of the majority element side by side, then we skip
# at the very least another number which makes the counter hit 0 for the last element if the rest of the
# majority element is dispersed evenly, in which case the last element is the majority element
# i.e. [1,1,3,3,1]

#2. the counter hits 0 by the last element which is the majority element if its dispersed evenly
# i.e. [1,3,1,3,1]

#3. the counter doesnt hit 0 by the time you hit the last element, in which case you return the majority
# i.e. [1,1,1,3,3]

def BoyerMooreMajorityElement(nums):
    maj = nums[0]
    counter = 1
    for x in nums:
        if x != maj:
            counter-=1
            if counter==0:
                maj = x
                counter = 1
        else:
            counter+=1
    return maj

print(BoyerMooreMajorityElement([8,8,8,8,1,1,1])) #8
