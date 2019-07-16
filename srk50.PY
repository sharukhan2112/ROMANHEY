power1=int(input())
flag=0
while power1!=1:
    if power1==0:
        print("no")
        flag=1
        break
    if power1%2!=0:
        print("no")
        flag=1
        break
    power1=power1//2
if(flag==0):
    print("yes")
