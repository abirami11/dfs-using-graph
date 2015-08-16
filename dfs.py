class TreeNode:
	def __init__(self, key, left=None,right=None,parent = None):
		self.leftChild = left
		self.rightChild = right
		self.keyValue = key
		self.parent = parent

	def hasleftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def binary_insert(self,key):
		if self.keyValue:
			if key <= self.keyValue :
				if self.hasleftChild() :
					self.leftChild.binary_insert(key)
				else:
					self.leftChild = TreeNode(key)
			else:
				if self.hasRightChild():
					self.rightChild.binary_insert(key)
				else:
					self.rightChild = TreeNode(key)
		else:
			self = TreeNode(key)

	def dfs(self):
		print self.keyValue
		if self.leftChild:
			self.leftChild.dfs()
		if self.rightChild:
			self.rightChild.dfs()
	
	def dfs_stack(self):
		stack = [self]
		while stack:
			node = stack.pop()
			print node.keyValue
			if node.rightChild:
				stack.append(node.rightChild)
			if node.leftChild:
				stack.append(node.leftChild)
			


node = TreeNode(10)
node.binary_insert(8)
node.binary_insert(13)
node.binary_insert(9)
node.binary_insert(12)
node.binary_insert(15)
node.binary_insert(7)
#node.display_tree()
node.dfs_stack()