from itertools import product
n=int(input())
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


ans=[]
s=ten_to_n(n,2)
one=0
dic={}

for i in range(len(s)):
    if s[i]=="1":
        dic[one]=i
        one+=1

for p in product([0,1],repeat=one):
    now=list(s)
    for i in range(one):
        if p[i]==1:
            now[dic[i]]="1"
        else:
            now[dic[i]]="0"
    ans.append("".join(now))
         
for i in range(len(ans)):
    print(n_to_ten(int(ans[i]),2))
