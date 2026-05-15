n,d=map(int,input().split())
s=list(input())
nokori=0
for i in range(d):
    for j in range(n-1,-1,-1):
        if s[j]=="@":
            s[j]="."
            break

print("".join(s))