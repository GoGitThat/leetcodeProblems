#link to problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/

def findDirection(arr, ind):
    #return True if going left, else return False to go right
    if arr[ind-1] > arr[ind] and arr[ind+1] < arr[ind]:
        return True
    if arr[ind-1] < arr[ind] and arr[ind+1] > arr[ind]:
        return False

def isPeak(arr, ind):
    #return true if peak
    if arr[ind-1] < arr[ind] and arr[ind] > arr[ind+1]:
        return True
    return False

def peakIndexInMountainArray(arr):
    start,end = 0,len(arr)-1

    while start<=end:
        middle = (start+end)//2
        if isPeak(arr, middle):
            return middle
        else:
            if findDirection(arr, middle):
                end = middle-1
            else:
                start = middle+1
    return 1

print(peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])) #2
print(peakIndexInMountainArray([0,10,5,2])) #1
