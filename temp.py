def change_greedy(coins, value):
    n = len(coins)
    
    # coin_counts is the counts of coins you are using
    # coin_counts[i] = count(coin[i])
    coin_counts = [0]*len(coins)
    
    # Implement the greedy version as described in pdf
    # Remember to add to coin_counts[i] for coins[i], when appropriate
    
    ######################
    ### YOUR CODE HERE ###
    ######################
    
    i = n - 1;
    while (i >= 0):
        while(value >= coins[i]):
            value -= coins[i];
            coin_counts.append(coins[i]);
        
        i -= 1
    
    # return the counts
    # will be converted in get_result_greedy()
    return coin_counts
    
coins = [1, 10, 25, 50] 
value = 40
print(change_greedy(coins, value));
