s1=int(input())
arr=list(map(int,input().split()[:s1]))
rra=sorted(arr,reverse=True)
print(rra[0])
