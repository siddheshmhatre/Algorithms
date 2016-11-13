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

	list_x = []
	list_y = []
	obtain_alignment(A, X, Y, len(X), len(Y), list_x, list_y)

	list_x.reverse()
	list_y.reverse()

	print ''.join(list_x) + '\n' + ''.join(list_y)

	return A[len(X)][len(Y)]

def obtain_alignment(A, X, Y, x_idx, y_idx, list_x, list_y):

	# Handle base cases
	if x_idx == 0 and y_idx == 0:
		return 

	if x_idx == 0:
		y_idx -= 1
		while y_idx >= 0:
			list_x.append('-')
			list_y.append(Y[y_idx])
			y_idx -= 1
		return 

	if y_idx == 0:
		x_idx -= 1
		while x_idx >= 0:
			list_y.append('-')
			list_x.append(X[x_idx])
			x_idx -= 1
		return

	# Recursively compute optimal sequence alignment
	p_gap = 6
	p_mismatch = 5 if X[x_idx-1] != Y[y_idx-1] else 0
	if A[x_idx][y_idx] == p_mismatch + A[x_idx-1][y_idx-1]:
		list_x.append(X[x_idx-1])
		list_y.append(Y[y_idx-1])
		obtain_alignment(A, X, Y, x_idx-1, y_idx-1, list_x, list_y)
	elif A[x_idx][y_idx] == p_gap + A[x_idx - 1][y_idx]:
		list_x.append(X[x_idx - 1])
		list_y.append('-')
		obtain_alignment(A, X, Y, x_idx-1, y_idx, list_x, list_y)
	else:
		list_x.append('-')
		list_y.append(Y[y_idx - 1])
		obtain_alignment(A, X, Y, x_idx, y_idx-1, list_x, list_y)

def main():
	print 'Test case 1 -  {}'.format(seq_align('AGGGCT','AGGCA'))
	print 'Test case 2 -  {}'.format(seq_align('','AGGCA'))
	print 'Test case 3 -  {}'.format(seq_align('AGGGCT',''))

if __name__ == "__main__":
	main()
