def insertion_sort(arr):
	for i in range(1,len(arr)):
		currentval=arr[i]
		position=i
		while position>0 and arr[position-1]>currentval:
			arr[position]=arr[position-1]
			position=position-1
		arr[position]=currentval
			
