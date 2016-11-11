from directed_graph import DiGraph
from copy import deepcopy

def bellman_ford(graph, s):
	nodes = graph.nodes.keys()
	A = [[0] * len(nodes) for i in range(2)]
	nodes.remove(s)
	for node in nodes:
		A[0][node-1] = float('inf')
	
	for i in range(1,len(nodes)+2):
		for node in nodes:
			w = find_incoming_nodes(graph,node)
			min_innodes = min(map(lambda x: graph.nodes[x][node] + A[0][x-1], w)) 
			A[1][node-1] = min(A[0][node-1], min_innodes)
		diff = sum(A[0]) - sum(A[1])  
		A[0] = deepcopy(A[1])

	if diff != 0:
		return 'Negative cycle'
	else:
		return A[1]

def find_incoming_nodes(graph,node):
	incoming_nodes = []
	for ele in graph.nodes.keys():
		if node in graph.nodes[ele]:
			incoming_nodes.append(ele)
	return incoming_nodes

if __name__ == '__main__':
	nodes = [1,2,3,4,5]
	#edges = [(1,2,2),(2,3,2),(3,4,2),(5,4,4),(1,5,4),(2,5,1)]
	edges = [(1,2,2), (3,2,4), (2,5,-4), (5,4,3), (4,3,5)]
	graph = DiGraph()
	graph.add_nodes(nodes)
	graph.add_edges(edges)
	print bellman_ford(graph, 1)
	
