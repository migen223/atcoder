

n,m=map(int,input().split())
a=list(map(int,input().split()))

se=set()
for i in range(n):
    se.add(len(str(a[i])))
    #print(str(a[i]))
ketal=list(se)

l=[[] for i in range(11)]

for i in ketal:
    dic={}
    for j in range(n):
        num=(a[j]*10**i)%m
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    l[i].append(dic)
"""    
print(ketal)
print(l)
print(l[1],l[2])
"""

modl=[a[i]%m for i in range(n)]

ans=0

for i in range(n):
    leng=len(str(a[i]))
    #print(l[leng][0],modl[i])
    if m-modl[i] in l[leng][0]:
        ans+=l[leng][0][m-modl[i]]
    elif modl[i]==0:
        if 0 in l[leng][0]:
            ans+=l[leng][0][0]
print(ans)

"""
for i in range(n):
    for j in range(n):
        if int(str(a[i])+str(a[j]))%m==0:
            print(a[i],a[j])
"""

