s=input()
a=[0,0,0]
for i in range(len(s)):
    if s[i]=="A":
        a[0]+=1
    if s[i]=="B":
         a[1]+=1
    if s[i]=="C":
        a[2]+=1
if a[0]==a[1]==a[2]==1:
    print("Yes")
else:
    print("No")