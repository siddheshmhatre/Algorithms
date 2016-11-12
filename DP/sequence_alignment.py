# compute optimal value after optimal sequence alignment
def seq_align(X,Y):
	A = [[0] * (len(Y)+1) for i in range(len(X)+1)]

	# Penalty of 6 for a gap and 5 for mismatch
	p_gap = 6
	p_mismatch = 5

	# Compute value iteratively using recurrence
	for i in range(1,len(X)+1):
		A[i][0] = i * p_gap
	for j in range(1,len(Y)+1):
		A[0][j] = i * p_gap
	for i in range(len(X)):
		for j in range(len(Y)):
			A[i+1][j+1] = min((p_mismatch if X[i]!=Y[j] else 0) + A[i][j], p_gap + A[i][j+1], p_gap + A[i+1][j])

	return A[len(X)][len(Y)]

def main():
	print seq_align('AGGGCT','AGGCA')

if __name__ == "__main__":
	main()
