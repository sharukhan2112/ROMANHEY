ee1=int(input())
fl=0
if ee1>2:
    for i in range(3,int(ee1/2)):
        if ee1%i==0:
            fl=1
            print("no")
            break
if fl==0 or ee1==2:
    print("yes")
