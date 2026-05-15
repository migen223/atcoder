n=int(input())
ans=""
for i in range(n):
    if (i+1)%3==0:
        ans+="x"
    else:
        ans+="o"
print(ans)