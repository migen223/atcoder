n,t,a=map(int,input().split())
nokori=n-(t+a)
if min(t,a)+nokori>max(t,a):
    print("No")
else:
    print("Yes")