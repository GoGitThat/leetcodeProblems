#link to problem: https://leetcode.com/problems/rotate-image/

#the algorithmn as follows:
# for every pair of numbers where the row and column index isn't the same,
# we want to swap their indices and put them in the new spot
# then we iterate through every row, swapping the elements at we iterate inwards
# see the example below to see why it works

#        |1      2       3|           |7      4       1|
#        |4      5       6|           |8      5       2|
# input: |7      8       9| result:   |9      6       3|

# so we will iterate through matrix: 1,2,3...9
#we come across 1, since the column and row indexes match, we leave it alone
#we come across 2, its pair is (0,1), its complement in position is 4 at (1,0) so we swap the 2 with 4

#        |1      4       3|
#        |2      5       6|
# swap:  |7      8       9|

#we come across 3, its pair is (0,2), its complement in position is 7 at (2,0) so we swap the 3 with 7

#        |1      4       7|
#        |2      5       6|
# swap:  |3      8       9|


#we come across 2 again, but since we've already processed it's pair, we can leave it alone (aka skip it)
#this is why we only process elements where row index < column index or vice versa since for each
#pair of elements we only need to swap them once, for my solution I used row index < column

#we come across 5, since the column and row indexes match, we leave it alone
#we come across 6, its pair is (1,2), its complement in position is 8 at (2,1) so we swap the 6 with 8

#        |1      4       7|
#        |2      5       8|
# swap:  |3      6       9|

#we come across 3 again, but since we've already processed it's pair, we can leave it alone (aka skip it)
#we come across 6 again, but since we've already processed it's pair, we can leave it alone (aka skip it)
#we come across 9, since the column and row indexes match, we leave it alone

#           |1      4       7|
#           |2      5       8|
# current:  |3      6       9|

#now we iterate through all the rows and swap each pair of elements starting from the ends of each row

#   swap:   |1      4       7| -> |7    4    1|
#           |2      5       8| -> |8    5    2|
#           |3      6       9| -> |9    6    3|

#and we have our result.



def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i < j:
                a = matrix[i].pop(j)
                b = matrix[j].pop(i)
                matrix[i].insert(j, b)
                matrix[j].insert(i, a)
    for k in range(len(matrix)):
        reverse_list(matrix[k])
    return matrix

def reverse_list(mylist):
    count = 0
    i,j = 0,0
    while mylist and count < (len(mylist)//2):
        a = mylist.pop(i)
        b = mylist.pop(-1-j)
        mylist.insert(i, b)
        mylist.insert(len(mylist)-j, a)
        i+=1
        j+=1
        count+=1

print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
# [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
