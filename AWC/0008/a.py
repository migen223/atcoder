import sys
n,w,k=map(int,input().split())

if w//(n-1)>=k:
    print("Yes")
else:
    print("No")
    