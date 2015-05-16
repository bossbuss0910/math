import matplotlib.pyplot as plt

def prime(value):
	for num in range(2,value):
		if value%num==0:
			return -1
	return 1
list=[]
for num in range(2,100000):
	if prime(num)>0:
		list.append(num)
print list
list2=[]
for num in list:
	list2.append(1.0/num)
list3=[]
sum=0
for num in list2:
	sum=sum+num
	list3.append(sum)
plt.plot(list3)
plt.show()
