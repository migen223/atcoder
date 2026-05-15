n,t=map(int,input().split())
score=[0]*n
se=set()
se.add(0)
dic={0:n}
ans=1
ansl=[]
for i in range(t):
    a,b=map(int,input().split())
    if score[a-1]+b in se:
        dic[score[a-1]+b]+=1
    else:
        dic[score[a-1]+b]=1
        se.add(score[a-1]+b)
        ans+=1
    dic[score[a-1]]-=1
    if dic[score[a-1]]==0:
        dic.pop(score[a-1])
        se.remove(score[a-1])
        ans-=1
    score[a-1]+=b
    ansl.append(ans)
for i in ansl:
    print(i)
