# Knapsack algorithm
def knapsack(values, size, capacity):

	# Create matrix of size (n+1) * (capacity+1) where n is # of items
	V =[ [0] * (capacity + 1) for i in range (len(values)+1)]

	for i in range(0,len(values)):
		for j in range(1,capacity+1):
			if j - size[i] >= 0 :
				V[i+1][j] = max(V[i][j], values[i] + V[i][j-size[i]])
			else:
				V[i+1][j] = V[i][j]

	knapsack_items(V, values, size, len(values), capacity)

	return V[len(values)][capacity]

def knapsack_items(V, values, size, n, cap):
	
	# Recursively obtain knapsack items
	if n == 0 or cap == 0:
		return 
	if V[n][cap] == V[n - 1][cap - size[n-1]] + values[n-1]:
		print 'Item:{}'.format(n)
		knapsack_items(V, values, size, n-1, cap - size[n-1])
	else:
		knapsack_items(V, values, size, n-1, cap)

def main():
	values, size, capacity = [3,2,4,4], [4,3,2,3], 6
	print knapsack(values, size, capacity)

if __name__ == "__main__":
	main()
