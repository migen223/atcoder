n,c1,c2=input().split()
n=int(n)
s=list(input())
for i in range(n):
    if s[i]!=c1:
        s[i]=c2
print("".join(s))