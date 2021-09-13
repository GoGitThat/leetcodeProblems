#link to problem: https://leetcode.com/problems/counting-bits/

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    if n == 0:
        return [0]
    if n==1:
        return [0,1]

    myl = [0,1]

    for x in range(2,n+1):
        if (x & (x-1)) == 0:
            myl.append(1)
        else:
            myl.append(myl[x//2] + (x%2))
    return myl


print(countBits(2)) #[0,1,1]
print(countBits(5)) #[0,1,1,2,1,2]
