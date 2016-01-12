f=open("tenpuzzle.txt")
data=f.read()
f.close()
write=open("tenpuzzle2.txt","w")
number=data.split("\n")
for num in number:
	if len(num)!=0:
		write.write(num+"\n")
