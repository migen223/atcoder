
n=int(input())
a=list(map(int,input().split()))
l=[0]

for i in range(n):
    for j in range(len(l)):
        l[j]=(a[i]+l[j])%360
    l.append(0)

l.sort()
l.append(360)
#print(l)
ansl=[]
for i in range(len(l)-1):
    ansl.append(abs(l[i]-l[i+1]))
print(max(ansl))


