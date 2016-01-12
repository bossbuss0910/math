def Coupon_kind(index):
	if index==0:
		return 500
	elif index==1:
		return 200
	elif index==2:
		return 100
	else:
		print "error"

def select(amount,Coupon_list):
	if amount<=1000 or sum(Coupon_list)==0:
		return[0,0,0]
	else:
		use_Coupon=[]
		for index,num in enumerate(Coupon_list):
			count=0
			for k in range(num):
				if amount-Coupon_kind(index)<0:
					use_Coupon.append(count)
					break
				amount=amount-Coupon_kind(index)
				count=count+1
				if k==num-1:
					use_Coupon.append(count)
		return use_Coupon

print select(1210,[2,1,3])
