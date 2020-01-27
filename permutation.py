def permute(s):
	out=[]
	if len(s)==1:
		return s
	else:
		for i,j in enumerate(s):
			for k in permute(s[:i]+s[i+1:]):
				print('per:',k)
				out+=[j+k]
	return out
print(permute('abc'))