n=int(input())
s1l=[0]
s2l=[0]
s1=0
s2=0
for i in range(n):
    c,p=map(int,input().split())
    if c==1:
        s1+=p
    else:
        s2+=p
    s1l.append(s1)
    s2l.append(s2)
    
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(f"{s1l[r]-s1l[l-1]} {s2l[r]-s2l[l-1]}")

