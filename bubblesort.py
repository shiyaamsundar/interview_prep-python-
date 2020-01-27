def bubblesort(arr):
	for i in range(len(arr)-1,0,-1):
		for j in range(i):
			if arr[j]>arr[j+1]:
				temp=arr[k]
				arr[k]=arr[k+1]
				arr[k+1]=temp
	return arr

