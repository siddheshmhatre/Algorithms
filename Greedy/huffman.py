from binarytree import Node
import heapq

def huffman_encoding(alphabet):
	nodes = createNodes(alphabet)
	heap = []
	for item in alphabet.items():
		heapq.heappush(heap, (item[1],item[0]))
	while len(nodes) > 1:
		min_1 = heapq.heappop(heap)
		min_2 = heapq.heappop(heap)
		heapq.heappush(heap,(min_1[0] + min_2[0], min_1[1] + min_2[1]))
		node = Node(min_1[1] + min_2[1])
		node.right = nodes[min_1[1]]
		node.left = nodes[min_2[1]]
		nodes[node.value] = node
		del nodes[min_1[1]]
		del nodes[min_2[1]]

	return nodes.items()[0][1]

def createNodes(alphabet):
	nodes = {}
	for ele in alphabet.keys():
		nodes[ele] = Node(ele)
	return nodes

if __name__ == "__main__":
	alphabet = {'A': 3, 'B':2, 'C':6, 'D':8, 'E':2, 'F':6}
	print huffman_encoding(alphabet)
