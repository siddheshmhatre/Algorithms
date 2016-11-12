from collections import defaultdict
import random

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
		M[j] = min([penalty(i,j,M) for i in range(1,j+1)])
	
	find_segments(M, error, C, len(points))

	return M[-1]

def compute_error(points):
	
	error = defaultdict(lambda: defaultdict(float))

	# Compute a, b according to closed form solution
	def compute_a_b(i, j, points_slice):
		size = j - i + 1
		x_sum = sum(x[0] for x in points_slice)
		y_sum = sum(x[1] for x in points_slice)
		num = size * sum(x[0] * x[1] for x in points_slice) - x_sum * y_sum 
		den = size * sum(x[0] ** 2 for x in points_slice) - x_sum ** 2
		a = num / float(den)
		b = (y_sum - a * x_sum) / size
		return a,b

	# Iterate through all possible i<=j and compute 
	# least squares error
	for size in range(0,len(points)):
		for i in range(len(points) - size):
			if size == 0:
				error[i][i] = 0.0
			else:
				j = i + size
				points_slice = points[i:j+1]
				a, b = compute_a_b(i, j, points_slice)
				error[i+1][j+1] = sum([(x[1] - a*x[0] - b) ** 2 for x in points_slice])
	
	return error

def find_segments(M, error, C, j):
	
	# Recursively find the line segements using M
	min_val = float('inf')
	min_idx = None
	if j == 0:
		return
	else:
		for i in range(j,0,-1):
			tmp = min(min_val, error[i][j] + C + M[i-1])
			if tmp < min_val:
				min_idx = i
			min_val = tmp

		if j == min_idx:
			print 'Line Segment: {}, {}'.format(min_idx-1,j)
		else:
			print 'Line Segment: {}, {}'.format(min_idx,j)

		find_segments(M, error, C, min_idx-1)

def main():
	points = [(1,3), (2,1), (3,3)]
	print points
	error = compute_error(points)
	C = 1
	M = segmented_least_squares(points, C)

if __name__ == "__main__":
	main()
