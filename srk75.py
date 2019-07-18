ss11=input()
n2=len(ss11)
if n2%2!=0:
    ss11=ss11[:int(n2/2)]+'*'+ss11[int(n2/2)+1:n2]
else:
    ss11=ss11[:int(n2/2)-1]+'**'+ss11[int(n2/2)+1:n2]
print(ss11)
