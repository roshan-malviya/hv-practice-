def sum_pairs(arr,k):
	main_lis=[]
	for i in range(len(arr)):
		f=[]
		for j in range(i,len(arr)):
			if arr[i]> k:
				break
			elif arr[i]+arr[j]==k:
				f.append(arr[i])
				f.append(arr[j])
				main_lis.append(f)
	return(main_lis)


print(sum_pairs([2,3,4,0,5,6,1],3))
