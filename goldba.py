#-*- coding:utf-8 -*-

def prime(value):
	for num in range(2,value):
		if value%num==0:
			return -1
	return 1
def search(list,tar):
	for num in list:
		if tar-num in list:
			return num
	return 0

def main():
	list=[]
	tar=2014
	for num in range(2,tar):
		if prime(num)>0:
			list.append(num)
	print list
	ans=search(list,tar)
	if ans==0:
		print "なかったよ！"
	else:
		print ans,"と",tar-ans
if __name__ == '__main__':
    main()
