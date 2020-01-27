##soln 1

# def anagrams(s1,s2):
# 	s1=s1.replace(' ','').lower()
# 	s2=s2.replace(' ','').lower()
# 	return sorted(s1)==sorted(s2)

# print(anagrams('god','dog'))

##soln 2
def anagrams(s1,s2):
	s1=s1.replace(' ','').lower()
	s2=s2.replace(' ','').lower()
	if len(s1)!=len(s2):
		return False
	else:
		count={}
		for i in s1:
			if i in count:
				count[i]+=1
			else:
				count[i]=1
		for i in s2:
			if i in count:
				count[i]-=1
			else:
				count[i]=1
		F=0
		for i in count:
			if count[i]!=0:
				 F=1
		if F!=1:
			return True
		else:
			return False


			

print(anagrams('dog','god'))


