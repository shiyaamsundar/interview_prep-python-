# class Stack(object):
# 	def __init__(self):
# 		self.items=[]
# 	def push(self,item):
# 		self.items.append(item)
# 	def pop(self):
# 		return self.items.pop()
# 	def peek(self):
# 		return self.items[len(self.items)-1]
# 	def size(self):
# 		return len(self.items)
def check(s):
	if len(s)%2!=0:
		return False
	opening=list('({[')
	matches=set([('(',')'),('[',']'),('{','}')])
	stack=[]
	for i in s:
		if i in opening:
			stack.append(i)
		else:
			if len(stack) ==0:
				return False
			
			last_open=stack.pop()
			if (last_open,i) not in matches:
				return False
	return len(stack)==0



print(check('[(]'))

