import random

class HashTable(object):

	def __init__(self):
		self.size = 10
		self.table = [[] for x in range(self.size)]
		self.data_size = 0
	
	def hashfunction(self,x): return x % self.size

	def insert_data(self,idx,ele): self.table[idx].append(ele)

	def insert(self,data):
		self.data_size += len(data)

		if self.data_size / float(self.size) > 9:
			data += [item for sublist in self.table for item in sublist]
			self.size = max(self.data_size / 10, self.size * 2)
			self.table = [[] for x in range(self.size)]

		for ele in data:
			self.insert_data(self.hashfunction(ele),ele)
	
	def retrieve_item(idx):
		return self.table[hashfunction]
	
if __name__ == "__main__":
	a = HashTable()
	data = [random.randint(0,10) for x in range(10)]
	print data
	a.insert(data)
	data = [random.randint(0,10) for x in range(10)]
	print data
	a.insert(data)
	print a.table
	print len(a.table)
	print a.data_size
