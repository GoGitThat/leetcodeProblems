#link to problem: https://leetcode.com/problems/spiral-matrix/

#here is the more "straight-forward" solution:
# the idea is simple, if the row count is 1, process the top layer else process the bottom layer
# go left to right for the top layer and then downwards starting from the "-1" side of the arrays
# in between the top and bottom layer, increment row count and process the bottom layer, do the same
# except iterate from right "-1" to left and then in the between layers between bottom and top this time
# iterating the left borders of the arrays (0 onwards) and continue until we run out of "total_elems"


def spiralOrder(matrix):
    layer = 1
    spiral = []
    col_count = len(matrix[0])
    max_row = len(matrix)
    total_elems = max_row * col_count
    row_count = 1
    while row_count <= len(matrix):
        if row_count % 2 == 0:
            for x in range(col_count-layer, layer-2, -1):
                spiral.append(matrix[layer*-1][x])
            if len(spiral) < total_elems:
                for y in range(max_row-layer, layer, -1):
                    spiral.append(matrix[y-1][layer-1])
            else:
                return spiral
            row_count+=1
            layer+=1
        else:
            for x in range(layer-1, col_count - layer +1, 1):
                spiral.append(matrix[layer-1][x])
            if len(spiral) < total_elems:
                for y in range(layer, max_row-layer, 1):
                    spiral.append(matrix[y][layer*-1])
            else:
                return spiral
            row_count+=1
    return spiral

##this is the smarter solution but uses alot more space compared to the constant space above:
# what it does is, it pops the first array from the matrix everytime, then transposes it and reverses it and repeats
# from the pop step, but it works if you trace the following example:
# [[1,2,3],[4,5,6],[7,8,9]] -> pop [1,2,3]
# [[6,9],[5,8],[4,7]] -> transposed and reversed
# [[5,8],[4,7]] -> pop [6,9]
# [[8,7],[5,4]] -> transposed and reversed
# ...
# [[5]] -> last pop
#
# |1      2       3|
# |4      5       6|
# |7      8       9| -> spiral, we trace top row -> [1,2,3]
#
# |6      9|
# |5      8|
# |4      7| -> [6,9] now technically is the first row, however compared to the original matrix, we can see
# that it represents going down the right side, so this transpose and reverse makes sense and we just keep repeating

def spiralOrderTransposeMethod(matrix):
    spiral = []
    while matrix:
        spiral.extend(matrix.pop(0))
        if matrix:
            matrix = [[row[-1-i] for row in matrix] for i in range(len(matrix[0]))]
    return spiral

print(spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))
#[1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2]
print(spiralOrderTransposeMethod([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))
#[1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2]
