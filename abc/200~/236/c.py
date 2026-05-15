
n,m=map(int,input().split())
s=input().split()
t=set(input().split())

for i in range(n):
    if s[i] not in t:
        print("No")
    else:
        print("Yes")


