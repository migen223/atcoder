
n=int(input())
s=input()
w=list(map(int,input().split()))


dic={}
change={0:1,1:-1}
for i in range(n):
    if w[i] not in dic:
        dic[w[i]]=change[int(s[i])]
    else:
        dic[w[i]]+=change[int(s[i])]

ans=0
for i in range(n):
    if s[i]=="1":
        ans+=1
w=list(set(w))

w.sort()
now=ans
for i in range(len(w)):
    now+=dic[w[i]]
    ans=max(ans,now)
    #print(now)
#print(dic)
print(ans)



