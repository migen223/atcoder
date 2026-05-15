import sys
s,t,k=map(int,input().split())

num=0
for i in range(k+1):
    if s*pow(2,i)==t:
        print(i)
        sys.exit()

print(-1)