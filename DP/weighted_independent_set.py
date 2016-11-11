def wis(weights):
	A = []
	A.append(weights[0])
	A.append(max(weights[0],weights[1]))
	for i in range(2,len(weights)):
		A.append(max(A[i-1],A[i-2] + weights[i]))
	return A[len(weights)-1]

if __name__ == "__main__":
	weights = [1,4,5,4]
	print wis(weights)
