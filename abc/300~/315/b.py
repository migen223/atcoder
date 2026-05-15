m=int(input())
d=list(map(int,input().split()))

y=sum(d)
day=(y+1)//2
count=0
mo=0
for i  in range(m):
    count+=d[i]
    if count>=day:
        count-=d[i]
        mo=i
        break
print(mo+1,day-count)
