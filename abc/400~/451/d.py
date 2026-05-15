
n=int(input())

pl=[set() for _ in range(10)]
q=1
count=0
while q<=10**9:
    pl[len(str(q))].add(q)
    q*=2

    
for i in range(2,10):
    for j in range(1,i):
        for k in pl[j]:
            for l in pl[i-j]:
                pl[i].add(k*(10**(i-j))+l)
        #print(pl)

ans=[]
for i in range(1,10):
    for j in pl[i]:
        ans.append(j)
ans.sort()
#print(ans)
#print(len(ans))
#print(ans)
print(ans[n-1])
#print(pl)

