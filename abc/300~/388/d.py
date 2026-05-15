
n=int(input())
a=list(map(int,input().split()))

plus=[0]*n
minus=[0]*(n+1)
minus[min(a[0]+1,n)]=-1
for i in range(1,n):
    plus[i]=plus[i-1]+minus[i]+1
    minus[min(i+a[i]+plus[i]+1,n)]-=1

for i in range(n):
    print(max(0,plus[i]+a[i]-(n-i-1)),end=" ")
print()
#print(plus)
#print(minus)





