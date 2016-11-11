class Graph(object):

	def __init__(self):
		self.nodes = {}
		self.edges = []
	
	def add_nodes(self, nodes):
		for node in nodes:
			self.add_node(node)
	
	def add_node(self,node):
		if node not in self.nodes:
			self.nodes[node] = {}
		else:
			raise Exception('{0} already present'.format(node)) 
	
	def add_edges(self,edges):
		self.edges = edges
		for edge in edges:
			self.add_edge(edge)

	def add_edge(self,edge):
		u,v, weight = edge
		if (v not in self.nodes[u]) and (u not in self.nodes[v]):
			self.nodes[u][v] = weight
			if u!=v:
				self.nodes[v][u] = weight

	def get_graph(self):
		return self.nodes

	def neighbors(self,node):
		return self.nodes[node]
