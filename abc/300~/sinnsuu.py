def ten_to_n(num,n):#numをn進数に変換　返り値はstr
    if num==0:
        return "0"
    else:
        k=0
        while n**k<=num:
            k+=1
        ans=[]
        rang=k
        for i in range(rang):
            k-=1
            keta=num//(n**k)
            num-=keta*(n**k)
            ans.append(str(keta))
        return "".join(ans) 
def n_to_ten(num,n):#num(n)を10進数に変換　返り値はstr
    s=str(num)
    ans=0
    k=0
    for i in range(len(s)):
        ans+=int(s[-1-i])*n**k
        k+=1
    return str(ans)

print(n_to_ten(int(input()),5))
"""
9=1*2^3+0*2^2+0*2^1+1*2^0
"""