n=int(input())
i=input()
l=list(map(int,i.split()))
s=0
for a in range(0,n,2):
    s+=l[a]

print(s)