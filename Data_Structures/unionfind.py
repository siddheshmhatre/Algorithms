class UnionFind(object):

	def __init__(self, nodes):
		self.elements = {}
		self.groups = {}
		for node in nodes:
			self.elements[node] = node
			self.groups[node] = [node]
	
	def find(self,node):
		return self.elements[node]

	def union(self, u, v):
		leader_u = self.elements[u]
		leader_v = self.elements[v]
		if len(self.groups[leader_u]) > len(self.groups[leader_v]):
			self.merge(leader_u,leader_v)
		else:
			self.merge(leader_v,leader_u)
	
	def merge(self, node1, node2):
		for ele in self.groups[node2]:
			self.elements[ele] = node1
		self.groups[node1] += self.groups[node2]
		del self.groups[node2]

if __name__ == '__main__':
	a = UnionFind([1,2,3,4])
	a.union(1,2)
	a.union(1,3)
	print a.find(3)
	print a.find(2)
	print a.find(1)
	print a.find(4)
	print a.groups
