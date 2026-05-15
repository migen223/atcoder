from sortedcontainers import SortedSet, SortedList, SortedDict

n=int(input())
x=list(map(int,input().split()))
dic={}
s=SortedList([x[0],0])

ans=2*x[0]
print(ans)
dic[0]=abs(x[0])
dic[1]=abs(x[0])

point={}
people={}
for i in range(n):
    people[i+1]=x[i]
    point[x[i]]=i+1
people[0]=0
point[0]=0

#dicがそれぞれの人のd
#peopleがそれぞれの人の番号から座標
#pointが逆


for i in range(1,n):
    ind=s.bisect_left(x[i])
    if ind==i+1:
        last=s[ind-1]
        lastpeople=point[last]
        #print(f"{lastpeople} {last} last")
        dic[i+1]=x[i]-last
        if dic[lastpeople]>x[i]-last:
            ans-=dic[lastpeople]-(x[i]-last)
            dic[lastpeople]=x[i]-last
        ans+=dic[i+1]
    else:
        pre=s[ind-1]
        next=s[ind]
        prepeople=point[pre]
        nextpeople=point[next]
        #print(f"{pre} {prepeople} pre")
        #print(f"{next} {nextpeople} nex")
        if dic[prepeople]>x[i]-pre:
            ans-=dic[prepeople]-(x[i]-pre)
            dic[prepeople]=x[i]-pre
        if dic[nextpeople]>abs(x[i]-next):
            ans-=dic[nextpeople]-abs(x[i]-next)
            dic[nextpeople]=abs(x[i]-next)
        ans+=min(abs(x[i]-pre),abs(x[i]-next))
        dic[i+1]=min(abs(x[i]-pre),abs(x[i]-next))
    print(ans)
    #print(dic)
    #print(s)
    s.add(x[i])
