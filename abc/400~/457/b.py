
n=int(input())

ll=[]
for i in range(n):
    l=list(map(int,input().split()))
    a=l[1:]
    l=l[0]
    ll.append(a)

x,y=map(int,input().split())
print(ll[x-1][y-1])