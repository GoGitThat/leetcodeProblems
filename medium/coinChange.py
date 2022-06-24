#link to problem: https://leetcode.com/problems/coin-change/

# the premise to this problem is that each total amount is composed of smaller total amounts
# for example, say we have the following coin denominations [1,5,10] and the amount target is 10
# well 10 can be made with 5 - pennies, 1 - nickel but how do we get there? 

# Total[10] = some_coin + F[current_amount-some_coin], F[current_amount-some_coin] represents the amount of coins needed to 
# reach the value of the target -  the value of the current coin we are on.

# So the idea is to build a map of the number of coins it takes to reach each total prior to our target and use that to determine the 
# minimum number of coins needed to hit our target.


def coinChange(coins, amount):
    #set a default high amount (greater than amount)
    dfs = [amount+1] * (amount+1)
    #you need 0 coins to hit 0 total
    dfs[0] = 0
    #calculate the number of coins it takes for each amount leading to our required total
    for amounts in range(1, amount+1):
        #of all the coin options, if subtracting a coin value is greater than 0, calculate the minimum between the current
        #dfs[amount] or the current coins 1 + dfs[amount-coin], so this implies the minimum solution will trend towards 1 + dfs[amount-coin] approaching 0
        #since that is where our minimum will lie
        for coin in coins:
            if amounts - coin >= 0:
                dfs[amounts] = min(dfs[amounts], 1 + dfs[amounts-coin])
    #if the dfs amount is still the default, then we haven't found the combination, else return the combination
    return dfs[amount] if dfs[amount] != (amount+1) else -1

print(coinChange([1,2,5], 11)) #3

