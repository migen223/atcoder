n=int(input())
a=list(map(int,input().split()))

print(a[0],end=" ")
for i in range(n-1):
    if abs(a[i]-a[i+1])>1:
        if a[i]>a[i+1]:
            for j in range(a[i]-1,a[i+1]-1,-1):
                print(j,end=" ")
        else:
            for j in range(a[i]+1,a[i+1]+1):
                print(j,end=" ")
    else:
        print(a[i+1],end=" ")
print()