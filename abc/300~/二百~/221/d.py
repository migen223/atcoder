n=int(input())
days=[]
se=set()
people=[]
for i in range(n):
    a,b=map(int,input().split())
    people.append((a,a+b))
    if a not in se:
        days.append(a)
        se.add(a)
    if a+b not in se:
        days.append(a+b)
        se.add(a+b)
days.sort()

dic={}
dic2={}
for i in range(len(days)):
    dic[days[i]]=i
    dic2[i]=days[i]

imos=[0]*(len(days))

for i in range(n):
    imos[dic[people[i][0]]]+=1
    if dic[people[i][1]]!=len(days):
        imos[dic[people[i][1]]]-=1
    
ansl=[imos[0]]
for i in range(1,len(imos)):
    ansl.append(ansl[-1]+imos[i])

ansd={}
for i in range(len(ansl)-1):
    num=dic2[i+1]-dic2[i]
    if ansl[i] not in ansd:
        ansd[ansl[i]]=num
    else:
        ansd[ansl[i]]+=num
if ansl[-1] not in ansd:
    ansd[ansl[-1]]=1
else:
    ansd[ansl[-1]]+=1

#print(days,dic,imos,ansl)
#print(ansd)

for i in range(1,n+1):
    if i in ansd:
        print(ansd[i],end=" ")
    else:
        print(0,end=" ")

print()


