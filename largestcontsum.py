def sum(a1):
	if len(a1)==0:
		return
	max_sum=cur_sum=0
	for i in a1[1:]:
		cur_sum=max(cur_sum+i,i)
		max_sum=max(cur_sum,max_sum)
	return max_sum
	