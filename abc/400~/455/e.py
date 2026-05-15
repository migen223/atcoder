from collections import Counter
n=int(input())
s=input()
r=[[0,0,0]]
dic={"A":0,"B":1,"C":2}
for i in range(n):
    now=r[-1][:]
    now[dic[s[i]]]+=1
    r.append(now)

subl=[[0]*(n+1) for i in range(4)] #a-b,b-c,a-c,(a-b,b-c)
subl[3][0]=(0,0)
for i in range(1,1+n):
    subl[0][i]=r[i][0]-r[i][1]
    subl[1][i]=r[i][1]-r[i][2]
    subl[2][i]=r[i][0]-r[i][2]
    subl[3][i]=(r[i][0]-r[i][1],r[i][1]-r[i][2])

ans=n*(n+1)//2
ab=Counter(subl[0])
bc=Counter(subl[1])
ac=Counter(subl[2])
abc=Counter(subl[3])

def count(dic):
    res=0
    for i in dic:
        res+=dic[i]*(dic[i]-1)//2
    return res

ans+=-count(ab)-count(bc)-count(ac)+2*count(abc)
print(ans)

