sab11,sab2=map(int,input().split())
p13=sab11*sab2
for i in range(0,p13+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
