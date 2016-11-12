"""
Segmented Least Squares problem as described in Algorithm Design, Kleinberg and Tardos
"""

def segmented_least_squares(points, C):

	M = [0] * (len(points) + 1)
	
	# Compute least squares error for all segments with start index i
	# end index j and i<=j and return dictionary 
	error = compute_error(points)

	# Function to compute penalty for a particular partition
	penalty = lambda x,y,z: error[x][y] + C + z[x-1]

	for j in range(1,len(M)):
		M[j] = min([penalty(i,j,M) for i in range(1,j+1)]

	return M[-1]

def compute_error(points):
	
	error = {}

	# Compute a, b according to closed form solution
	def compute_a_b(i,j):
		points_slice = points[i:j+1]
		size = j - i + 1
		x_sum = sum(x[0] for x in points_slice)
		y_sum = sum(x[1] for x in points_slice)
		num = size * sum(x[0] * x[1] for x in points_slice) - x_sum * y_sum 
		den = size * sum(x[0] ** 2 for x in points_slice) - x_sum ** 2
		a = num / float(den)
		b = (y_sum - a * x_sum) / n
		return a,b

	# Iterate through all possible i<=j and compute 
	# least squares error
	for size in range(1,len(points)):
		for i in range(len(points) - size):
			j = i + size
			a, b = compute_a_b(i,j)
			error[i+1][j+1] = sum([(x[1] - a*x[0] - b) ** 2 for x in points[i:j+1])
