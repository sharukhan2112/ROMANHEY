number1=int(input())
sum=0
if number1>0:
  digit=number1%10
  sum+=digit
  number1=number1//10
print(sum)
