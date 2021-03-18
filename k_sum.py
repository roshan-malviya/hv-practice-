def pairs(arr,k):

	a=[]
	for i in arr:
		n=[]
		for j in arr:
			if i+j==k:
				n.append(i)
				n.append(j)
			a.append(n)
	return(a)


print(pairs([1,5,3,2,6,0],6))
