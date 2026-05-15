
n=int(input())

doukasen=[]
second=[]

for i in range(n):
    doukasen.append(list(map(int,input().split())))
    second.append(doukasen[-1][0]/doukasen[-1][1])

s=sum(second)

time=s/2
ans=0

for i in range(n):
    if time-second[i]>0:
        ans+=doukasen[i][0]
        time-=second[i]
    else:
        ans+=time*doukasen[i][1]
        print(ans)
        break


