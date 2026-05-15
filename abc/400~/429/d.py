from bisect import bisect_left
from collections import Counter
n,m,C=map(int,input().split())
a=list(map(int,input().split()))

c=Counter(a)

sortp=sorted(list(set(a)))

sc=sorted(c.items(),key=lambda x:x[0])
l1=[sc[i][1] for i in range(len(sortp))]
circle=[l1[i%len(l1)] for i in range(2*len(l1))]
r=[circle[0]]
for i in range(1,2*len(sortp)):
    r.append(r[-1]+circle[i])

if sortp[0]!=0:
    sortp.insert(0,0)
    r.insert(0,0)
ansl=[]
for i in range(len(sortp)):
    ind=bisect_left(r,C+r[i])
    ansl.append(r[ind]-r[i])


ans=0

sortp.append(m)
#print(ansl)
#print(sortp)

for i in range(len(ansl)):
    ans+=ansl[i]*(sortp[i+1]-sortp[i])
print(ans)

    

"""
people=[]
peoplen=[]

dic={}

for i in range(n):
    if a[i] not in dic:
        dic[a[i]]=1
    else:
        dic[a[i]]+=1
#print(dic)
ss=sorted(dic.items(),key=lambda x:x[0])
#print(ss) 
if ss[0][0]==0:
    for i in range(1,len(ss)):
        people.append(ss[i][1])
        peoplen.append(ss[i][0])
    people.append(ss[0][1])

    
else:
    for i in range(len(ss)):
        people.append(ss[i][1])
        peoplen.append(ss[i][0])

circle=[0,people[0]]
for i in range(1,len(people)):
    circle.append(circle[-1]+people[i])


while len(circle)<=5*10**5+1:
    for i in range(len(people)):
        circle.append(circle[-1]+people[i])

for i in range(10):
    print(circle[i],end=" ")


now=0
ans=0

dic1={}
ansl=[]
for i in range(len(people)):
    ind=bisect_left(circle,now+c)
    #ans+=circle[ind]-now
    ansl.append(circle[ind]-now)
    dic1[people[i]]=circle[ind]-now
    now+=people[i]

print(ansl)
print(peoplen)
#print(ans)
peoplen.append(m)


ans+=circle[bisect_left(circle,c)]*(peoplen[0])
for i in range(len(peoplen)-1):
    if peoplen[i+1]-peoplen[i]>=2:
        ans+=(peoplen[i+1]-peoplen[i]-1)*dic[people[i]]

print(ans)



"""