import random

def merge(a,b):

	c = []
	i = j = 0
	for k in range(len(a) + len(b)):
		if a[i] < b[j]:
			c.append(a[i])
			i += 1
			if i == len(a):
				for p in range(j,len(b)):
					c.append(b[p])
				return c
		else :
			c.append(b[j])
			j += 1
			if j == len(b):
				for p in range(i,len(a)):
					c.append(a[p])
				return c
	return c

def mergesort(A):
	
	n = len(A)
	if n == 1:
		return A
	else:
		a = mergesort(A[:n/2])
		b = mergesort(A[n/2:])
		return merge(a,b)

if __name__ == "__main__":

	# Generate 10 random numbers
	unsorted = []
	for i in range(10):
		unsorted.append(random.randint(0,100))
	print unsorted
	sorted = mergesort(unsorted)
	print sorted
