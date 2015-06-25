#coding=utf-8
import time
#和
value=int(raw_input())

#input数
input_line=int(raw_input())

#棒の値
bar=[]
for k in range(input_line):
	input_linek=int(raw_input())
	bar.append(input_linek)

start=time.time()

bar.sort(reverse=True)

#答え
ans=0

def number_count(value,bar,count):
	if len(bar)==0 or count==3:
		return 
	for num in bar:
		k=value-num
		if  k==0 and count==2:
			global ans
			ans=ans+1
			return 
		num_list=[]
		for num_p in bar[bar.index(num)+1:]:
			if num_p<=k:
				num_list.append(num_p)
		number_count(k,num_list,count+1)

number_count(value,bar,0)
print ans
elapsed_time = time.time() - start
print elapsed_time

