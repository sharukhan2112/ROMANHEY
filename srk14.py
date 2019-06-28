n,q1=map(int,input().split())
if(q1<=100000):
    for x in range(n+1,q1):
        if(x%2!=0):
          print(x,end=" ")
