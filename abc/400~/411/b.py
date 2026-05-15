n=int(input())-1
d=list(map(int,input().split()))
for i in range(n):
    s=0
    for j in range(n-i):
        s+=d[i+j]
        print(s,end=" ")
    print("")