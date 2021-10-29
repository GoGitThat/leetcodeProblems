#link to problem: https://leetcode.com/problems/set-matrix-zeroes/

#solution explained:

# Going through the matrix and setting already visited elements/or the forward elements may cause
# unnecessary zeroing, especially if you have to revisit the elements, since there would be no indication
# if they were zero'd due to being 0 or due to a 0 in their column/row.

#i.e. |1 2 9 5 0 4 6|
#     |1 2 9 5 9 4 6|  cant 0 the column/row values because they arent visited yet
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|

# so the solution is to store the zero'd columns/rows in cells that we have already visited/know
# will be zero'd. If we do this in an array we end up with an (m+n) space solution

#we can store these in the same matrix: for rows we would store the value in the first cell of the row

#i.e. |1 2 9 5 0 4 6| store the 0  in the first cell -> |0 2 9 5 0 4 6|
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|

#we can store these in the same matrix: for columns we would store the value in the top cell of the
#column with the 0

#i.e. |1 2 9 5 0 4 6| store the 0  in the first cell, since it's already visited, it doesnt matter -> |0 2 9 5 0 4 6|
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|
#     |1 2 9 5 9 4 6|

#then we iterate backwards starting from the end of the matrix and we simply check if the first cell of the row or
#the top of the column is zero, if it is, then we set the current element to 0
#if the column is 0, we need to store the "column is 0" value in a separate variable since that cell would be shared by
#the row is 0 indicator and column is 0 indicator, so when column is 0, we simply check the "zero_col" variable to see if its 0

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_lim = rows-1
    cols_lim = cols-1
    zero_col = 1
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                if col==0:
                    zero_col = 0
                else:
                    matrix[0][col] = 0
                matrix[row][0] = 0
    for row in range(row_lim, -1, -1):
        for col in range(cols_lim, -1, -1):
            if col==0:
                if zero_col==0:
                    matrix[row][col] = 0
            else:
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col] = 0
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]])) #[[1,0,1],[0,0,0],[1,0,1]]
