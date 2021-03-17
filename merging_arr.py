def merger(arr1,ar2):
	ar1=arr1+ar2	
	for i in range(len(ar1)):
		for j in range((len(ar1)-1)-i):
			if ar1[j]>ar1[j+1]:
				ar1[j],ar1[j+1]=ar1[j+1],ar1[j]
	return ar1

b=list(map(int,input().split()))
c=list(map(int,input().split()))
print(merger(b,c))