n=int(input())
namelist=[]
for i in range(n):
    name=input().split()
    namelist.append(name)

flag1=0
flag2=0
for i in range(n):
    for j in range(n):
        if i!=j and namelist[i]==namelist[j]:
            flag1=1
            flag2=1
    if flag1==1:
        break
if flag2==1:
    print("Yes")
else:
    print("No")