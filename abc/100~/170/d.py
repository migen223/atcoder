n=int(input())
a=list(map(int,input().split()))
ma=max(a)
count=[0]*(ma+1)
for ai in a:
    count[ai]+=1

for ai in a:
    if count[ai]==0:
        continue
    if count[ai]>1:
        count[ai]=0
    k=2
    while ai*k<=ma:
        count[ai*k]=0
        k+=1
#print(count)
print(sum(count))