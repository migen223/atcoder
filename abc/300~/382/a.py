n,d=map(int,input().split())
s=input()
nokori=0
for i in range(n):
    if s[i]=="@":
        nokori+=1

print(n-nokori+d)