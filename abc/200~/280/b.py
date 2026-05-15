
n=int(input())
s=list(map(int,input().split()))
ans=[s[0]]
for i in range(1,n):
    
    ans.append(s[i]-s[i-1])
    #print(ans)
print(*ans)