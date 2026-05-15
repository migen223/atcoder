
n=int(input())
a=list(map(int,input().split()))
odd=[]
even=[]
for i in range(n):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
even.sort()
odd.sort()
ans=-1
if len(odd)>=2:
    ans=max(ans,odd[-1]+odd[-2])
if len(even)>=2:
    ans=max(ans,even[-1]+even[-2])
print(ans)