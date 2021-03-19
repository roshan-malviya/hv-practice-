#                     'method #1'


#                                                method1





def check1(arr):
	first_ele=arr[0]
	last_ele=arr[-1]
	e=0
	k=[]
	while first_ele<=last_ele:
		if first_ele==arr[e]:
			first_ele+=1
			e+=1
		else:
			first_ele+=1
			k.append(first_ele-1)
	return k




#                                                method1


#                                                method2





def check2 (arr):
	missing_ele=[]
	for i in range(len(arr)-1):
		if arr[i]-arr[i+1]!=1:
			if arr[i]-arr[i+1]==2:
				missing_ele.append(arr[i]+1)
			else:
				for k in range(arr[i]+1,arr[i+1]):
					missing_ele.append(k)
	return missing_ele


b=list(map(int,input().split(',')))


print('first method',check1(b))
print('second method',check2(b))









