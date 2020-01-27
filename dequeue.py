class Deque(object):
	def __init__(self):
		self.items=[]
	def addrear(self,item):
		self.items.insert(0,item)
	def isempty(self):
		return self.items==[]
	def addfront(self,item):
		self.items.append(item)
	def removefront(self):
		return self.items.pop()
	def removerear(self):
		return self.items.pop(0)
	def size(self):
		return len(self.items)