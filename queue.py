class Queue(obejct):
	def __init__(self):
		self.items=[]
	def isempty(self):
		return self.items==[]
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeuq(self):
		return self.item.pop()
	def size(self):
		return len(self.items)