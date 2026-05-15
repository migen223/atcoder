from collections import Counter
s=input()
n=len(s)

c=Counter(list(s))
ans=0
for i in c.most_common():
    if i[1]>=3:
        ans+=(i[1]*(i[1]-1)*(i[1]-2))//6
#print(ans)
dic={}
for i in range(n):
    if s[i] in dic:
        dic[s[i]].append(i)
    else:
        dic[s[i]]=[i]
#print(dic)
for i in dic:
    if len(dic[i])>=3:
        now=dic[i][0]
        l=[]
        for j in range(1,len(dic[i])):
            l.append(dic[i][j]-now-1)
            now=dic[i][j]
        r=[0]
        for j in range(len(l)):
            r.append(r[-1]+l[j])
        #print(l)
        if len(l)%2==0:
            for j in range(len(l)//2):
                ans+=(len(l)-2*(j))*(r[-1-j]-r[j])
        else:
            for j in range(len(l)//2+1):
               # print(f"afbh {(len(l)-2*(j))*(r[-1-j]-r[j])}")
                ans+=(len(l)-2*(j))*(r[-1-j]-r[j])
    elif len(dic[i])==2:
        ans+=dic[i][1]-dic[i][0]-1
    #print(ans)
print(ans)
