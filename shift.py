# @@@@@@@@@@@@@@@@ reversing and shifting an array in left direction @@@@@@@@@@@@
arr=[3,9,5,7,2]
minel=arr[0]
for i in range((len(arr)-1)):
	if minel>arr[i+1]:
		minel,arr[i+1]=arr[i+1],minel
print(arr)