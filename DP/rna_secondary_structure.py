"""
RNA secondary structure problem as described in Algorithm Design, Kleinberg and Tardos
"""

# Method to compute optimal no. of pairings
def rna_opt_sec_val(strand):

	n = len(strand)

	# Create a n * n matrix
	A = [[0] * n for i in range(n)]

	# Check contiguous interval of length k > 5
	for k in range(5,n):
		for i in range(0, n-k):
			j = i + k

			# Base case for smallest contiguous interval 
			if k == 5 and canPair(strand[i], strand[j]):
				A[i][j] = 1

			# Use recurrence to get optimal value for 
			# current interval
			else:
				val2 = 0
				for t in range(i,j - 4):
					if canPair(strand[t], strand[j]):
						if t == i:
							val2 = max(val2, 1 + A[t+1][j-1])
						else:
							val2 = max(val2, 1 + A[i][t-1] + A[t+1][j-1])

				A[i][j] = max(A[i][j-1], val2)
	return A

# Method to recover pairing and index of respective bases
def recover_pairings(strand, A, start, end):

	# Base case
	if start > end - 4:
		return

	# No. of pairings if end doesn't take part 
	val1 = A[start][end-1]
	val2 = 0
	match = None

	# Get no. of pairings if end pairs with t
	# s.t. t < j - 4
	for t in range(start,end):
		if t < end - 4 and canPair(strand[t], strand[end]):
			if t == start:
				temp = max(val2, 1 + A[t+1][end-1])
			else:
				temp = max(val2, 1 + A[start][t-1] + A[t+1][end-1])
			if temp > val2:
				match = t
			val2 = temp

	if val1 > val2:
		recover_pairings(strand, A, start, end - 1)
	else:
		if match!=None:
			# Print pairing if present in optimal solution
			# and recurse on two subproblems
			print strand[match], match, strand[end], end
			recover_pairings(strand, A, start, match - 1)
			recover_pairings(strand, A, match + 1, end - 1)

# Method to check if bases pair
def canPair(x,y):
	if (x == 'A' and y == 'T') or (x == 'T' and y == 'A') or (x == 'C' and y == 'G') or (x == 'G' and y == 'C'):
		return True
	else:
		return False

def main():

	strand = 'ACGTCGATTCGAGCGAATCGTAACGATACGAGCATAGCGGCTAGAC'
	opt_val = rna_opt_sec_val(strand)
	print 'No of pairings{}'.format(opt_val[0][len(strand) - 1])
	recover_pairings(strand, opt_val, 0, len(strand) - 1)

if __name__ == "__main__":
	main()
