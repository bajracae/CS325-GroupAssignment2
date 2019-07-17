
import sys
# Use Dynamic Programming to find the minimum number of coins

# ans is the coins you are using, returned by change_dp()
def get_result_dp(ans, value):
    count = value
    coins_used = []
    while count > 0:
        print(ans[count])
        coins_used.append(ans[count])
        count = count - ans[count]
    return coins_used

# dynamic programming implementation
def change_dp(coins, value): 
    
    n = len(coins)
    
    # table[i] will be storing the minimum 
    #   number of coins required for value i 
    table = [0 for i in range(value + 1)]

    # ans[i] will be the coins array index of first coin
    #   you make change with at value i
    # we fill with -1 for non-existent values
    ans = [-1 for i in range(value + 1)]

    # Base case (If given value is 0)
    # Can't make change for 0 
    table[0] = 0

    # Initialize all table values as infinite
    for i in range(1, value + 1): 
        table[i] = sys.maxsize 


    # Compute minimum coins required 
    # for all values i from 1 to value
    # Be sure to store the first coin you use at each i value

    for i in range(1, value + 1): 
          
        # Go through all coins smaller than i 
        for j in range(len(coins)): 
            if (coins[j] <= i): 
                sub_res = table[i - coins[j]] 
                if (sub_res != sys.maxsize and 
                    sub_res + 1 < table[i]): 
                    table[i] = sub_res + 1
                    ans[i] = coins[j]
    ######################
    ### YOUR CODE HERE ###
    ###################### 
    
    # return minimum coins and the coins we used

    return table[value], ans


# Test your DP implementation
# It should pass assert statements
def test_dp():
    coins = [1, 10, 25, 50]  
    value = 40
    
    num_coins, ans = change_dp(coins, value)
    coin_usage = get_result_dp(ans, value)
    
    assert num_coins == 4, 'Wrong number of coins'
    print(coin_usage)
    assert coin_usage == [10, 10, 10, 10], 'Wrong coin types'
    assert sum(coin_usage) == value, 'Incorrect change value'
    
    print('Value: {}, Number of coins: {}, Coins used: {}'.format(value, len(coin_usage), coin_usage)) 

test_dp()