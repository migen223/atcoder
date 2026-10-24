
n,x=input().split()
n=int(n)

dic={"A":0,"B":1,"C":2,"D":3,"E":4}

t=[]
for i in range(n):
    s=input()
    t.append(s)

c=0
for i in range(n):
    if t[i][dic[x]]=="o":
        c+=1
if c>0:
    print("Yes")

else:
    print("No")