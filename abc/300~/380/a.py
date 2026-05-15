n=input()
o=0
t=0
th=0
for i in range(len(n)):
    if n[i]=="1":
        o+=1
    elif n[i]=="2":
        t+=1
    elif n[i]=="3":
        th+=1
if o==1 and t==2 and th==3:
    print("Yes")
else:
    print("No")