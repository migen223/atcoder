
k=int(input())

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

s=ten_to_n(k,2)

ans=[]
for i in range(len(s)):
    if s[i]=="1":
        ans.append("2")
    else:
        ans.append("0")
print("".join(ans))

