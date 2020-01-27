def selection_sort(arr):
	for i in range(len(arr)-1,0,-1):
		pos_max=0
		for j in range(1,i+1):
			if arr[j]>arr[pos_max]:
				pos_max=j
		temp=arr[j]
		a[j]=arr[pos_max]
		a[pos_max]=temp
