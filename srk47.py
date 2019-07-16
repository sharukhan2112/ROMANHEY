number1=int(input())
for i in range(number1):
  num=list(map(int,input().split()))
  x=min(num)
  y=max(num)
  print(x,y)
