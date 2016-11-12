import sys
if "../" not in sys.path:
	sys.path.append("../")
from Graphs_and_Trees.directed_graph import DiGraph
from copy import deepcopy

# Method to compute single source shortest path distances
def bellman_ford(graph, s):
	nodes = graph.nodes.keys()

	# Create matrix of size 2 * len(nodes) for 
	# space optimization
	A = [[0] * len(nodes) for i in range(2)]
	nodes.remove(s)

	# Initialize base case
	for node in nodes:
		A[0][node-1] = float('inf') 
	
	# Compute distances and let it run for len(nodes)
	# iterations to check for negative cycle
	for i in range(1,len(nodes)+2):
		for node in nodes:
			w = find_incoming_nodes(graph,node)
			min_innodes = min(graph.nodes[x][node] + A[0][x-1] for x in w)
			#min_innodes = min(map(lambda x: graph.nodes[x][node] + A[0][x-1], w)) 
			A[1][node-1] = min(A[0][node-1], min_innodes)
		diff = sum(A[0]) - sum(A[1])  
		A[0] = deepcopy(A[1])

	# If shortest distances change after len(nodes) iterations
	# then negative cycle is detected
	if diff != 0:
		return 'Negative cycle'
	else:
		return A[1]

# Method to find all incoming nodes for a particular node
def find_incoming_nodes(graph,node):
	incoming_nodes = []
	for ele in graph.nodes.keys():
		if node in graph.nodes[ele]:
			incoming_nodes.append(ele)
	return incoming_nodes

def main():
	
	# nodes list
	nodes = [1,2,3,4,5]

	# Graph with no negative cycle
	graph = DiGraph()
	edges =	[(1,2,2), (2,3,2), (3,4,2), (5,4,4), (2,5,1), (1,5,4)]
	graph.add_nodes(nodes)
	graph.add_edges(edges)
	print bellman_ford(graph, 1)

	# Graph with negative cycle
	graph = DiGraph()
	edges =	[(1,2,2), (2,3,2), (3,4,2), (4,2,-5), (5,4,4), (2,5,1), (1,5,4)]
	graph.add_nodes(nodes)
	graph.add_edges(edges)
	print bellman_ford(graph, 1)

if __name__ == '__main__':
	main()
