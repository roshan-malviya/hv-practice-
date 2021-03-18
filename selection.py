def selection(arr):
	for i in range(len(arr)):
		mini=i
		for j in range(i+1,len(arr)):

			if arr[mini]>arr[j]:
				mini=j
		arr[i],arr[mini]=arr[mini],arr[i]
	return arr











a=[1,9,5,7,2,54 ]
print(selection(a))











# a=[2,4,3,7]
# mini=a[0]
# for i in range(len(a)-1):
# 	if mini>a[i+1]:
# 		mini=a[i+1]
# print(mini)