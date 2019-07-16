import sys

coins = [1, 10, 25, 50];
m = len(coins);
V = 40

# ===================OLD CODE=====================
# table = [[0 for x in range(m)] for x in range(n+1)]
# 
# for i in range(m):
# 	table[0][i] = 1
# 
# for i in range(1, n+1):
# 	for j in range(m):
# 		x = table[i - S[j]][j] if i-S[j] >= 0 else 0
# 
# 		y = table[i][j-1] if j >= 1 else 0
# 
# 		table[i][j] = x + y
# 
# print(table[n][m-1]);

# table[i] will be storing the minimum  
    # number of coins required for i value.  
    # So table[V] will have result 
	
	
table = [0 for i in range(V + 1)] 

# Base case (If given value V is 0) 
table[0] = 0

# Initialize all table values as Infinite 
for i in range(1, V + 1): 
    table[i] = sys.maxsize 

# Compute minimum coins required  
# for all values from 1 to V 
for i in range(1, V + 1): 
      
    # Go through all coins smaller than i 
    for j in range(m): 
        if (coins[j] <= i): 
            sub_res = table[i - coins[j]] 
            if (sub_res != sys.maxsize and 
                sub_res + 1 < table[i]): 
                table[i] = sub_res + 1
print(table[V]);