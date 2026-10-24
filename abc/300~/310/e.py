
n=int(input())
s=input()
zero=0
rle=[]
for i in range(n):
    if s[i]=="0":
        zero+=1
    if not rle:
        rle.append([s[i],1,i])
    else:
        if rle[-1][0]==s[i]:
            rle[-1][1]+=1
        else:
            rle.append([s[i],1,i])
ans=(n*(n+1))//2
ans-=zero


def calc(n):
    res=0
    if n%2==0:
        k=n//2-1
        res+=k*(k+1)+k+1
    else:
        k=n//2
        res+=k*(k+1)
    return res

for s,num,ind in rle:
    if s=="1":
        if ind!=0:
            ans-=num//2+calc(num)+(ind-1)*((num+1)//2)
        else:
            ans-=calc(num)
print(ans)
