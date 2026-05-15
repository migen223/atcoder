n,m=map(int,input().split())
s=0
for a in range(m+1):
    s+=n**a
    #print(n**a)

if s<=10**9:
    print(s)
else:
    print("inf")