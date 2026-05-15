n=int(input())
kyoten=[]
for i in range(n):
    w,x=map(int,input().split())
    kyoten.append([w,x])

ans=0
for i in range(24):
    people=0
    for j in range(n):
        if 9<=(kyoten[j][1]+i)%24<=17:
            people+=kyoten[j][0]
            #print(people,(kyoten[j][1]+i)%24)
    ans=max(ans,people)
print(ans)