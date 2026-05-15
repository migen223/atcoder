from collections import Counter
n=int(input())
ans=0
k=1

while True:
    quo=n//k
    mod=n%k
    change=mod//quo+1
    ans+=quo*change
    k+=change
    if quo==1:
        break
print(ans)
    


"""
s=set()
l=[]
for i in range(1,1+n):
    s.add(int(n/i))
    l.append(n//i)
print(sorted(list(s)))
print(len(s))
print(Counter(l))
"""