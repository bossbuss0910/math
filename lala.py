import fileinput
import math

def change(num,rem):
	num_st=str(num)
	new_num=num_st[rem:]
	print new_num
	num_in=float(new_num)
	return num_in


def func(a,x):
	ans=1
	for i in range(int(x)):
		ans=ans*a
		keta=int(math.log10(ans))+1
		if keta>8:
			ans=change(ans,keta-8)
	return ans


ans=[]

while 1:
	line=raw_input()
	number_st =line.split(" ")
	if number_st[0]=="0" and number_st[1]=="0":
		break
	ans.append(func(float(number_st[0]),int(number_st[1])))
for kotae in ans:
	print int(kotae)
