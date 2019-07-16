number1=int(input())
for i in range(number1):
  n=list(map(int,input().split()))
  avg=sum(n)//number1
  print(avg)
