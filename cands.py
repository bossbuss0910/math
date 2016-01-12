n=6
list=[]
def cut(number):
	num_str=str(number)
	X=num_str[:n/2]
	Y=num_str[n/2:]
	return int(X),int(Y)

def find(X,Y,num):
	if X**2+Y**2==num:
		print num
		list.append(num)

for num in range(10**(n-1),10**n):
	X,Y=cut(num)
	if Y>(10**(n/2))/2:
		continue
	find(X,Y,num)

print list
print sum(list)
