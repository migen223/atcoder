
n=int(input())
a=list(map(int,input().split()))
al=[[a[i],i] for i in range(n)]
al.sort(key=lambda x:x[0])

for i in range(3):
    print(al[i][1]+1,end=" ")
print()