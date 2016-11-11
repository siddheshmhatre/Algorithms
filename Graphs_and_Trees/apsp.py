from directed_graph import DiGraph
import pprint
from directed_graph import DiGraph
from bellman_ford import bellman_ford

def floyd_warshall(graph):
	nodes = graph.nodes.keys()
	edges = map(lambda x:(x[0],x[1]), graph.edges)
	n_nodes = len(nodes)
	A = [[[0] * (n_nodes) for i in range(n_nodes)] for j in range(n_nodes+1)]

	for i in range(n_nodes):
		for j in range(n_nodes):
			if i == j:
				val = 0
			else:
				if (i+1,j+1) in edges:
					val = graph.nodes[i+1][j+1]
				else:
					val = float('inf')
			A[0][i][j] = val

	for k in range(1,n_nodes+1):
		for i in range(n_nodes):
			for j in range(n_nodes):
				A[k][i][j] = min(A[k-1][i][j], A[k-1][i][k-1] + A[k-1][k-1][j])
				if k == n_nodes and i == j and A[k][i][j] < 0:
					return 'Negative Cycle'
	return A[n_nodes]

def johnson(graph):
	nodes = graph.nodes.keys()
	edges = graph.edges
	new_edges = []
	for node in nodes:
		new_edges.append((0,node,0))
	new_edges += edges
	nodes += [0]
	nodes.sort()
	graph_temp = DiGraph()
	graph_temp.add_nodes(nodes)
	graph_temp.add_edges(new_edges)
	dist = bellman_ford(graph_temp,0)
	dist.pop()	
	new_edges = []
	nodes.remove(0)
	for edge in edges:
		u,v,wt = edge
		new_edges.append((u,v,wt + dist[u-1] - dist[v-1]))
	print new_edges
	graph_temp = DiGraph()
	graph_temp.add_nodes(nodes)
	graph_temp.add_edges(new_edges())

	for node in nodes:
		pass
		#dist2.append(djikstra(graph,node))

	#adjust distances

if __name__ == '__main__':
	nodes = [1,2,3,4,5,6]
	#edges = [(1,2,2),(2,3,2),(3,4,2),(5,4,4),(1,5,4),(2,5,1)]
	#edges = [(1,2,2), (3,2,4), (2,5,-4), (5,4,3), (4,3,5)]
	edges = [(1,2,-2),(2,3,-1),(3,1,4),(3,6,-3),(5,6,-4),(5,4,1),(3,4,2)]
	graph = DiGraph()
	graph.add_nodes(nodes)
	graph.add_edges(edges)
	print johnson(graph)
