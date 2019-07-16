
# T: an array containing the values of the coins
# L: integer wich is the total to give back
# Output: Minimal number of coins needed to make a total of L
# https://gist.github.com/GabLeRoux/5398167
def count( T, L ):

	Opt = [0 for i in range(0, L+1)]
	
	n = len(T)
	for i in range(1, L+1):
		smallest = float("inf")
		for j in range(0, n):
			if (T[j] <= i):
				smallest = min(smallest, Opt[i - T[j]]) 
		Opt[i] = 1 + smallest 
	return Opt[L]

coins = [1, 10, 25, 50];
m = len(coins);
V = 40
print(count(coins, V))

# ===================THIS WORKS BUT HAS TO IMPORT SYS=====================
# import sys
# table = [0 for i in range(V + 1)] 
# 
# # Base case (If given value V is 0) 
# table[0] = 0
# 
# # Initialize all table values as Infinite 
# for i in range(1, V + 1): 
#     table[i] = sys.maxsize 
# 
# # Compute minimum coins required  
# # for all values from 1 to V 
# for i in range(1, V + 1): 
# 
#     # Go through all coins smaller than i 
#     for j in range(m): 
#         if (coins[j] <= i): 
#             sub_res = table[i - coins[j]] 
#             if (sub_res != sys.maxsize and 
#                 sub_res + 1 < table[i]): 
#                 table[i] = sub_res + 1
# print(table[V]);