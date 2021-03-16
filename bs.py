# def bs(arr,n):
# 	li=0
# 	ri=len(arr)-1
# 	mi=0
# 	while li<=ri:
# 		mi=(li+ri)//2
# 		mi_n=arr[mi]
# 		if mi_n==n:
# 			return mi
# 		if mi_n< n:
# 			li=mi+1
# 		else:
# 			ri=mi+1

# 	return False


a=[1,2,3,4,5,8,7]
# b=7
# print(bs(a,b))


def sorting_check(arr):
	# checking for accending ordere
	if a[0]<=a[1]:
		for i in range(len(a)-1):
			if a[i]<a[i+1]:
				pass
			else:
				return False
		return True
	else:
		for i in range(len(a)-1):
			if a[i]>a[i+1]:
				pass
			else:
				return False
		return True
print(sorting_check(a))