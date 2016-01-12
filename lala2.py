kugiri=4

line=raw_input()
input_list=[]
for index in range(int(line)):
	input_list.append(int(raw_input()))


def change(num,rem):
	num_st=str(num)
	new_num=num_st[len(num_st)-rem:]
	num_in=int(new_num)
	return num_in

fibo=[]
x=0
y=1
for var in range(100000000):
	if x >=10**kugiri:
		x=change(x,kugiri)
	if (x in fibo)and var>2:
		if fibo.index(x)+1==change(y,kugiri):
			print var
			break
	fibo.append(x)
	x, y = y, x + y
'''
for var in range(0,1500):
	if x >=1000:
		x=change(x,3)
	fibo.append(x)
	x,y=y,x+y
'''
print fibo
for ans in input_list:
	if ans>var:
		ans=ans%var
	print fibo[ans]

