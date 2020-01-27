def pair(arr,k):
	if len(arr)<2:
		return
	seen=set()
	output=set()
	for i in arr:
		target=k-i
		if target not in seen:
			seen.add(i)
			print('seen:',seen)
		else:
			output.add(((min(i,target)),max(i,target)))
			print('output:',output)
	return len(output),output


print(pair([1,3,2,2],4))
#print('\n'.join(map(str,list(output))))
