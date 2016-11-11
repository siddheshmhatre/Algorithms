def knapsack(values, size, capacity):
	V = []
	V =[ [0] * (capacity + 1) for i in range (len(values)+1)]
	for i in range(0,len(values)):
		for j in range(1,capacity+1):
			if j - size[i] >= 0 :
				V[i+1][j] = max(V[i][j], values[i] + V[i][j-size[i]])
			else:
				V[i+1][j] = V[i][j]
	return V

if __name__ == "__main__":
	print knapsack([3,2,4,4],[4,3,2,3],6)
