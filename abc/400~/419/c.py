from math import ceil,floor
n=int(input())
i=[]
j=[]
people=[]
for _ in range(n):
    r,c=map(int,input().split())
    i.append(r)
    j.append(c)
    people.append([r,c])
imin=min(i)
jmin=min(j)
for q in range(n):
    i[q]-=imin
    j[q]-=jmin
midup_x=ceil((max(i)+min(i))/2)
midup_y=ceil((max(j)+min(j))/2)
middown_x=floor((max(i)+min(i))/2)
middown_y=floor((max(j)+min(j))/2)
max1=-1
max2=-1
for k in range(n):
    a=max(abs(midup_x-i[k]),abs(midup_y-j[k]))
    b=max(abs(middown_x-i[k]),abs(middown_y-j[k]))
    #print(f"a={a}")
    #print(f"i={i[k]} {abs(mid_x-i[k])}")
    #print(f"j={j[k]} {abs(mid_y-j[k])}")
    if max1<a:
        max1=a
    if max2<b:
        max2=b
print(min(max1,max2))
