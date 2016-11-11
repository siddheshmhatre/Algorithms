class Node(object):
	
	def __init__(self,value):
		self.left = None
		self.right = None
		self.parent = None
		self.value = value

class BST(object):

	def __init__(self):
		self.root = None
	
	def add_nodes(self, vals):
		for value in vals:
			self.add_node(value)
	
	def add_node(self, value):
		new_node = Node(value)
		if self.root == None:
			self.root = new_node
		else:
			node = self.root
			while node and node.value != value:
				parent = node
				if node.value > value:
					node = node.left
				else: 
					node = node.right
			if parent.value >= value:
				parent.left = new_node
			else:
				parent.right = new_node
			new_node.parent = parent

	def search(self, root, value):
		if not root or root.value == value:
			return root
		if root.value < value:
			return self.search(root.right, value)
		else:
			return self.search(root.left, value)
	
	def find_element(self, value):
		return self.search(self.root,value)

	def find_min(self):
		return self.extremes(self.root)

	def find_max(self):
		return self.extremes(self.root,False)

	def extremes(self, root, min = True):
		while (min and root.left) or (not min and root.right):
			if min:
				root = root.left
			else:
				root = root.right
		return root

	def find_pred(self,value):
		root = self.find_element(value)
		if root.left:
			return self.extremes(root.left,False)
		else:
			parent = root.parent
			while parent:
				if parent.value <= value:
					return parent
				else:
					parent = parent.parent
			return root

	def traversal(self, order ='in'):
		values = []
		if order == 'in':
			self.in_order(self.root, values)
			return values
		elif order == 'pre':
			self.pre_order(self.root, values)
			return values
		elif order == 'post':
			self.post_order(self.root, values)
			return values
	
	def in_order(self, node, values):
		if node!=None:
			self.in_order(node.left, values)
			values.append(node.value)
			self.in_order(node.right, values)
	
	def pre_order(self, node, values):
		if node!=None:
			values.append(node.value)
			self.pre_order(node.left,values)
			self.pre_order(node.right,values)

	def post_order(self, node, values):
		if node!=None:
			self.post_order(node.left,values)
			self.post_order(node.right,values)
			values.append(node.value)
	
	def delete(self, value):
		node = self.find_element(value)
		print node.value
		if not node:
			return
		if not node.left and not node.right:
			parent = node.parent 
			if not parent:
				self.root = None
			else:
				parent.left = None
				parent.right = None
		elif not node.left and node.right:
			parent = node.parent
			if parent.left == node:
				parent.left = node.right
			else:
				parent.right = node.right
			node.right.parent = parent
		elif not node.right and node.left:
			parent = node.parent
			if parent.left == node:
				parent.left = node.left
			else:
				parent.right = node.left
			node.left.parent = parent
		else:
			new_root = self.extremes(node.right)
			temp = new_root
			parent = node.parent
			new_root.right = node.right
			new_root.left = node.left
			if not parent:
				self.root = new_root
			else:
				if parent.left == node:
					parent.left = new_root
				else:
					parent.right = new_root
			parent = temp.parent
			if parent.left == temp:
				parent.left = None
			else:
				parent.right = None
		
if __name__ == "__main__":
	tree = BST()
	vals = [3,1,2,5,4]
	tree.add_nodes(vals)
	print tree.delete(3)
	print tree.traversal(order = "in")
