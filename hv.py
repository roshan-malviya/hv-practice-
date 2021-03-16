

# #function for reversing an array
# def reve (arr):
#     for i in range (len(arr)//2):
#         arr[i],arr[-1-i]=arr[-1-i],arr[i]
#     return arr

# k=[1,2,3,4,5,6,7]

# print(reve(k))


# # function for searching an element in array

# def serach (arr,ele):
#     b=len(arr)//2
#     for i in range (b):
#         if arr[i]==ele or arr[i+b]==ele:
#             return True
#     return False

# a=[1,4,5,7,9,22,3,0,12]
# b=int(input('enter your number '))
# if len(a)%2!=0:
#     if a[len(a)//2+1]==b:
#         print ('yes')
#     elif serach(a,b):
#         print('yes')
#     else:
#         print ('no')
# elif serach(a,b):
#     print('yes')
# else:
#     print('no')


# function for largest number


def greatn (arr):
    j=arr[0]
    for i in range (len(arr)-1):
        if j<arr[i+1]:
            c=j
            j=arr[i+1]
    return (f'great value is {j} second greate value is {c}')

l=greatn([1,3,4,5,6,2,3,7])
print (l)
