n=int(input())
i=input()
l=list(map(int,i.split()))
s=0
s2=0
for c in range(0,n):
    s2+=l[c]
for a in range(n-1):
    s2=s2-l[a]
    s+=l[a]*s2


print(s) 
