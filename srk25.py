s1=int(input())
arr=list(map(int,input().split()[:s1]))
rra=sorted(arr)
print(rra[(int(len(arr)))//2])
