n2=list(input()) 
i=len(n2)-1
while len(n2)!=0:
    if n2[i]==n2[i-1]:
        n2.pop(i-1)
        for j in range(0,len(n2)): print(n2[j],end="")
        break
    i=i-1
