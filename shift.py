# @@@@@@@@@@@@@@@@ reversing and shifting an array in left direction @@@@@@@@@@@@


def shif(arr,m,direction):

	arr=arr[::-1]
	if direction=='left':
		return (arr[m::]+arr[:m:])

	else:
		right_end=arr[-m::]
		inde=arr[-m]
		p=arr.index(inde)
		left_end=arr[:p:]
		return (right_end+left_end)

print(shif([1,2,3,4,5,6],2,'right'))