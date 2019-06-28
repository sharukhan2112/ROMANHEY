n2=int(input(""))
if n2>1:
	for i in range (2,n2):
		if(n2%i)==0:
			print("no")
			break
	else:
		print("yes")
else:
	print("no")
