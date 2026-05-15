
n=int(input())

l=[]
for i in range(n):
    s=tuple(input().split())
    l.append(s)
l.sort(key=lambda x:int(x[1]),reverse=True)
#print(l)
print(l[1][0])
