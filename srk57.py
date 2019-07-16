x,z = map1(int,input().split())
c1 = list(map1(int,input().split()))
count=0
for j in c1:
    if (j==z):
       count+=1;
print(count)
