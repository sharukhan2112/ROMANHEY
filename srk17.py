num1=int(input())
s=num1
f=0
while(num1>0):
  var=num1%10
  num1=num1//10
  var2=var**3
  f=f+var2
if(s==f):
  print("yes")
else:
  print("no")
