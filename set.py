

# @@@@@@@@@@@@@@@@@@@@@@@@@function for uinion of an set@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def uinion (s1,s2):
	s=s1+s2
	main_s=[]
	for i in s:
		if i not in main_s:
			main_s.append(i)
	return (main_s)


# @@@@@@@@@@@@@@@@@@@@@@@@function for intersection @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def interS(s1,s2):
	main_s=[]
	for i in s1:
		for j in s2:
			if i==j:
				main_s.append(j)
				break
	return(main_s)

#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ function for difference @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def differ(ar1,ar2):
	k=[]
	for i in b:
		if i not in ar1:
			k.append(i)
	return k



a,b=[1,2,3],[2,3,5,2]

print(f'uinion of set is {uinion(a,b)} intersection is {interS(a,b)} difference is {differ(a,b)}')
