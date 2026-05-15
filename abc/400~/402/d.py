from collections import Counter
n,m=map(int,input().split())

line=[]
for i in range(m):
    a,b=map(int,input().split())
    line.append((a+b)%n)
c=Counter(line)
ans=0
#print(c)
for i in c:
    ans+=(m-c[i])*c[i]
    #print(ans)
print(ans//2)

