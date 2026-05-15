
n,k=map(int,input().split())
for i in range(1,10**6+1):
    si=(i*(n+n+i-1))//2
    #print(si)
    if si>=k:
        print(i-1)
        break
