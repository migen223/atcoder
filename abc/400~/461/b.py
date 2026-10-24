
import sys
n=int(input())
a=list(map(lambda x:int(x)-1,input().split()))
b=list(map(lambda x:int(x)-1,input().split()))

for i in range(n):
    if i!=b[a[i]]:
        print("No")
        sys.exit()

print("Yes")