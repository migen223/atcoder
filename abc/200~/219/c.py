x=list(input())
n=int(input())

dic={}
dic2={}
for i in range(26):
    dic[x[i]]=i
    dic2[i]=x[i]

nsort=[]
for i in range(n):
    s=list(input())
    l=[]
    for j in range(len(s)):
        l.append(dic[s[j]])
    nsort.append(l)
nsort.sort()
#print(nsort)
ans=[]
for i in range(n):
    l=[]
    for j in range(len(nsort[i])):
        l.append(dic2[nsort[i][j]])
    ans.append("".join(l))
for i in range(n):
    print(ans[i])

