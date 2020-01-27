def BinaryTree(r):
	return [r,[],[]]

def insertlefr(root,newbranch):
	t=root.pop(1)
	if len(t)>1:
		root.insert(1,[newbranch,t,[]])
	else:
		root.insert(1,[newbranch,[],[]])
	return root
def insertlefr(root,newbranch):
	t=root.pop(2)
	if len(t)>1:
		root.insert(2,[newbranch,[],t])
	else:
		root.insert(2,[newbranch,[],[]])
	return root
def getrootval(root):
	return root[0]
def setrootval(root,newval):
	root[0]=newval
def getleftchild(root):
	return root[1]
def getrightchild(root):
	return root[2]
	

