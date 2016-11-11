import random

def partition(A,l,r):
	piv = random.randint(l,r)
	temp = A[l]
	A[l] = A[piv]
	A[piv] = temp
	i = l + 1
	for j in range(l+1,r+1):
		if A[j] < A[l]:
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
			i = i + 1
	temp = A[i-1]
	A[i-1] = A[l]
	A[l] = temp
	return i-1

def quicksort (A,l,r):
	if r<l:
		return
	else:
		pos = partition(A,l,r)
		quicksort(A,l,pos-1)
		quicksort(A,pos+1,r)

if __name__ == "__main__":

	# Generate 10 random numbers
	unsorted = []
	for i in range(10):
		unsorted.append(random.randint(0,100))
	print unsorted
	quicksort(unsorted,0,len(unsorted)-1)
	print unsorted
