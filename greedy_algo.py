#change_val = 40;

#coin_types = [1, 10, 25, 50];
#list_len = len(coin_types);

#coin_list = [];

#i = list_len - 1;
#while(i >= 0):
#    while(change_val >= coin_types[i]):
#        change_val -= coin_types[i];
#        coin_list.append(coin_types[i]);
    
#    i -= 1

#for i in range(len(coin_list)):
#    print(coin_list[i], end = " ");

# Use Greedy to find the minimum number of coins

# this changes coin counts into the actual coins
def get_result_greedy(coin_counts, coins):
    coins_used = []
    for i in range(len(coin_counts)):
        for j in range(coin_counts[i]):
            coins_used.append(coins[i])
    return coins_used

# Greedy implementation
def change_greedy(coins, value):
    n = len(coins)
    
    # coin_counts is the counts of coins you are using
    # coin_counts[i] = count(coin[i])
    coin_counts = [0]*len(coins)
    
    # Implement the greedy version as described in pdf
    # Remember to add to coin_counts[i] for coins[i], when appropriate

    while(n >= 0):
        while(value >= coins[n-1]):
            value -= coins[n-1]
            coin_counts[n-1] += 1
        n -= 1
   
    # return the counts
    # will be converted in get_result_greedy()
    return coin_counts

def test_greedy():
    coins = [1, 10, 25, 50] 
    value = 40
    coin_counts = change_greedy(coins, value)
    num_coins = sum(coin_counts)
    coins_used = get_result_greedy(coin_counts, coins)
    assert num_coins == 7, 'Wrong number of coins'
    assert coins_used == [1, 1, 1, 1, 1, 10, 25], 'Wrong coins used'
    assert sum(coins_used) == value, 'Incorrect change value'
    print('Value: {}, Number of coins: {}, Coins used: {}'.format(value, num_coins, coins_used))
test_greedy()
