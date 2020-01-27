def rev(s):
	words=[]
	space=[' ']
	i=0
	while i<len(s):
		if s[i] not in space:
			start=i 
			while  i<len(s) and s[i] not in space:
				i+=1
			words.append(s[start:i])
			
		i+=1

	return " ".join(reversed(words))


print(rev("the  best  how are you"))