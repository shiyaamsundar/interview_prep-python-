class Queue2stack(object):
	def __init__(self):
		self.instack=[]
		self.outstack=[]
	def enqueue(self,ele):
		self.instack.append(ele)
	def dequeue(self):
		if not self.outstack:
			while  self.instack:
				self.outstack.append(self.instack.pop())
		return self.outstack.pop()
	


