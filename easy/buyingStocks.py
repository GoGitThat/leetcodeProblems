#link to problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    minDay = 99999999999999
    maxVal = 0
    for value in prices:
        if value < minDay:
            minDay = value
        if value - minDay > maxVal:
            maxVal = value - minDay
    return maxVal

print(maxProfit([7,1,5,3,6,4])) #5
print(maxProfit([7,6,4,3,1])) #0
