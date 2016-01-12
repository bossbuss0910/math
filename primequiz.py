import random

def is_prime3(q,k=50):
	q = abs(q)
	if q == 2: return True
	if q < 2 or q&1 == 0: return False
	d = (q-1)>>1
	while d&1 == 0:
		d >>= 1
	for i in xrange(k):
		a = random.randint(1,q-1)
		t = d
		y = pow(a,t,q)
		while t != q-1 and y != 1 and y != q-1: 
			y = pow(y,2,q)
			t <<= 1
		if y != q-1 and t&1 == 0:
			return False
	return True

def prime_list(upper):
	list=[]
	for num in range(2,upper):
		if is_prime3(num)>0:
			list.append(num)
	return list

ans_list=[]
for i in range(10):
	line=raw_input()
	ans_list.append(len(prime_list(int(line))))

for ans in ans_list:
	print ans

