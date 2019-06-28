s1=int(input())
arr=list(map(int,input().split()[:s1]))
rra=sorted(arr)
for i in rra:
    print(i,end=" ")
