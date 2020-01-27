#soln 1
# def find(a1,a2):
# 	a1.sort()
# 	a2.sort()

# 	for i,j in zip(a1,a2):
# 		if i!=j:
# 			return i
# 	return a1[-1]

# print(find([1,2,3,4,6],[3,7,2,1,4,6]))


#soln2
# import collections

# def find(a1,a2):
# 	d=collections.defaultdict(int)

# 	for i in a2:
# 		d[i]+=1
# 	for i in a1:
# 		if d[i]==0:
# 			return i 
# 		else:
# 			d[i]-=1


# print(find([1,2,3,4,6,5,7],[3,7,2,1,4,6]))


def find(a1,a2):
	res=0
	for i in a1+a2:
		res^=i
		print(res)
	return res
print(find([1,2,3,4,6,5,7],[3,7,2,1,4,6]))

