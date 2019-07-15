m = 0
n	 = 0
T2 = []

T = [[0 for x in range(m)] for x in range (n+1)]
for i in range(m):
	T[0][i] = 1

for i in range(1, n+1):
	for j in range(m):
		x = T[i - T2[j]][j] if i - T2[j] >= 0 else 0
		y = T[i][j-1] if j >= 1 else 0

		T[i][j] = x + y
	
	#return T[n][m-1]

arr = [1,2,3]
m = len(arr)
n = 4
print(arr,m,n)


