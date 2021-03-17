def merger(arr1,ar2):
	ar1=arr1+ar2	
	for i in range(len(ar1)):
		for j in range((len(ar1)-1)-i):
			if ar1[j]>ar1[j+1]:
				ar1[j],ar1[j+1]=ar1[j+1],ar1[j]
	return ar1

print(merger([1,2,8,4],[9,5,3,7]))