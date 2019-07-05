c1=input()
cou=0
for i in range(len(c)):
  if(c1[i].isdigit() or c1[i].isalpha() or c1[i]==(" ")):
    continue
  else:
    cou+=1
print(cou)
