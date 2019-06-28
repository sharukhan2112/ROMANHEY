s5=input()
flag=1
vow=['a','e','i','o','u']
for v in vow:
    if(s5==v):
        print("Vowel")
        flag=0
        break
if(flag):
    if(s5>='a' and s5<='z'):
        print("Consonant")
    else:
        print("invalid")
