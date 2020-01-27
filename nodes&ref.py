class BinaryTree(object):
	def __init__(self,rootobj):
		self.key=rootobj
		self.left=None
		self.right=None
	def insertleft(self,newNode):
		if self.left==None:
			self.left=BinaryTree(newNode)
		else:
			t=BinaryTree(newNode)
			t.left=self.left
			self.left=t



	def insertright(self,newNode):
		if self.right==None:
			self.right=BinaryTree(newNode)
		else:
			t=BinaryTree(newNode)
			t.right=self.right
			self.right=t
	def getrightchild(self):
		return self.right

	def getleftchild(self):
		return self.left

	def serrootval(self,obj):
		self.key=obj
	def getrootval(self):
		return self.key
	



