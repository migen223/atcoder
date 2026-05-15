def n_to_ten(num,n):#num(n)を10進数に変換　返り値はstr
    s=str(num)
    ans=0
    k=0
    for i in range(len(s)):
        ans+=int(s[-1-i])*n**k
        k+=1
    return str(ans)
k=int(input())
a,b=map(int,input().split())
a=int(n_to_ten(a,k))
b=int(n_to_ten(b,k))
print(a*b)