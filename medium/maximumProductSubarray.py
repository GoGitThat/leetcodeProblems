#link to problem: https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = max(nums)
    minn,maxx = 1,1
    
    for n in nums:
        if n==0:
            minn,maxx = 1,1
            continue
        tmp = n * maxx
        maxx = max(n * maxx, n * minn, n)
        minn = min(tmp, n * minn, n)
        ret = max(ret, maxx, minn)
    return ret