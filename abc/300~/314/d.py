n=int(input())
s=list(input())
q=int(input())
nochange=set()
f=1 #1の時何もいじらない、2の時小文字へ、3の時大文字へ
for i in range(q):
    t,x,c=input().split()
    x=int(x)
    if t=="2":
        f=2
        nochange=set()
        continue
    elif t=="3":
        f=3
        nochange=set()
        continue

    s[x-1]=c
    if f!=1:
        nochange.add(x-1)
    #print(f,nochange)
ans=[]
for i in range(n):
    #print(s[i])
    if f==2:
        if i in nochange:
            ans.append(s[i])
        else:
            ans.append(s[i].lower())
    elif f==3:
        if i in nochange:
            ans.append(s[i])
        else:
            ans.append((s[i].upper()))
    else:
        ans.append(s[i])
print("".join(ans))
"""
ans=""

for i in range(n):
    #print(s[i])
    if f==2:
        if i in nochange:
            ans+=s[i]
        else:
            ans+=(s[i].lower())
    elif f==3:
        if i in nochange:
            ans+=s[i]
        else:
            ans+=(s[i].upper())
    else:
        ans+=s[i]
print(ans)
"""


"""
TEEQUICKBROWMFiXJUGPFOVERTBELAZYDOG
TEEQUICKBROWMFiXJUGPFOVERTBELAZYDOG

"""