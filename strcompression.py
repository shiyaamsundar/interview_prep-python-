a=input()
# r=""
# l=len(a)
# if l==0:
# 	print(None)
# elif l==1:
# 	print(a)
# else:
# 	last=a[1]
# 	cnt=1
# 	i=1
# 	while i<l:
# 		if a[i]==a[i-1]:
# 			cnt+=1
# 		else:
			
# 			r=r+a[i-1]+str(cnt)
# 			cnt=1
# 		i+=1
# 	r=r+a[i-1]+str(cnt)
# print(r)
#method 2

# d={}
# l=[]
# r=""
# for i in a:
# 	if i not in l:
# 		l.append(i)
# 		d[i]=0
# for i in d.keys():
# 	for j in a:
# 		if i==j:
# 			d[i]+=1
# for i,j in d.items():
# 	r=r+i+str(j)


# print(d)
# print(r)
