def dup (arr):
	g=[]
	g1=[]
	for i in arr:
		if i in g and i not in g1:
			print (i)
			g1.append(i)
		else:
			g.append(i)

arr=[1,2,3,4,5,6,2,3,5,2]
dup(arr)
