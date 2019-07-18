ss11=int(input())
flag2=0
if(ss11>2):
    for i in range(2,int(ss11/2)+1):
        if ss11%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or ss11==2:
    print("no")
