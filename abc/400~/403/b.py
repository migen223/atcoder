t=input()
u=input()
ls=len(u)
f=0
for a in range(len(t)-ls+1):
    s=0
    if t[a]==u[0] or t[a]=="?":
        for b in range(1,ls):
            if t[a+b]==u[b] or t[a+b]=="?":
                s+=1
            
    if s==ls-1:
        print("Yes")
        f+=1
        break
if f==0:
    print("No")