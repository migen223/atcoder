n=int(input())
s=input()

for i in range(1,n):
    l=0
    for j in range(n):
        if j+i<=n-1:
            if s[j]==s[j+i]:
                break
            else:
                l+=1
        else:
            break
    print(l)