#link to problem: https://leetcode.com/problems/index-pairs-of-a-string/
#its a premium problem

#Suppose we have a text string and words (a list of strings), we have to find all
#index pairs [i, j] such that the substring text[i]...text[j] is in the list of words.
#So if the string is like "ababa" and words array is like ["aba", "ab"], then the output will be [[0,1], [0,2], [2,3], [2,4]].

def findPairs(s, strings, arr=[], offset=0):
    #if string is empty, return
    if not s:
        return None
    else:
        #iterate through the strings
        for x in strings:
            if x in s:
                #find the starting index in "s"
                s_index = s.find(x)
                #calculate the actual start index in the original string by adding the offset
                start = offset+s_index
                #calculate the actual end index in the original string by adding the offset
                end = offset+s_index+len(x)-1
                #trim the search string
                new_str = s[end-offset+1:]
                #remove strings that are already longer than our new search string
                new_strs = [y for y in strings if len(y) <= len(new_str)]
                #store the atual start and end coords if they dont exist
                s_indices = (start,end)
                if s_indices not in arr:
                    arr.append(s_indices)
                #cut the current string, and recurse on it
                findPairs(new_str, new_strs, arr, end+1)
    #some sort of "sorting algorithmn", here using quicksort
    quickSort(arr, 0, len(arr)-1)
    return arr

###########################################------QUICKSORT------##########################
def partition(arr, start, end):
    #will hold index of an element that is greater than our pivot (arr[end])
    #aka it has to track the number of elements that are smaller than our pivot
    #since the number_of_elements = our index of where the pivot should be, we can
    #just use it as our index at the end
    j = start
    for x in range(start,end):
        if arr[x][1] < arr[end][1]:
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

###########################################------TESTING------##########################
print(findPairs("ababa",["aba","ab"])) # [(0,1), (0,2), (2,3), (2,4)]
# print(quickSort([7, 5, 8, 2, 4, 1, 8, 6], 0, 7))
