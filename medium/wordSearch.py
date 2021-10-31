#link to problem: https://leetcode.com/problems/word-search/

#it is a recursive solution.
# we iterate through the board and as soon as we match the first letter we call the recursive search
# it checks whether the index of the letter into the word is greater than the length of the word, if it is
# then it implies we found all previous letter so we return True since we've found the word
# otherwise we check if we are even in the bounds of the board and if the letter even matches the current cell we are in,
# if not, we simply return false
# first we hold a pointer to the current cell's value, then we mark the cell with a non alphabet character to imply we have
# visited it (so in subsequent recursive calls we dont recurse on it -> aka return false on it)
# then we simply call our search function on the 4 cells surrounding the current one even if they may be out of bounds (in the next call
# they will return right away)
# we reset the board cell back to the original value(since the board needs to be reset for the parent function (exist) so that the next
# time another starting letter is found it sees the original board)
# the idx value is to trim the string down each time we find a matching letter(word[1:] would create a new string object for each recursive call)
# so this saves memory space and instead we just increase the idx

def exist(board, word):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == word[0]:
                if search(board, word, x, y, 0):
                    return True
    return False

def search(board, word, row, column, idx):
    if idx >= len(word):
        return True
    else:
        if column < 0 or column >= len(board[0]) or row < 0 or row >= len(board) or board[row][column]!=word[idx]:
            return False
        temp = board[row][column]
        board[row][column] = "*"
        found = search(board, word, row+1, column, idx+1) or search(board, word, row, column+1, idx+1) or search(board, word, row-1, column, idx+1) or search(board, word, row, column-1, idx+1)
        board[row][column] = temp
        return found

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
#"True"
