
n=int(input())
a=list(map(int,input().split()))

keta=[0]*(max(a)+1)

for i in range(n):
    keta[a[i]]+=1
ansi=[keta[max(a)]]
for i in range(len(keta)-2,0,-1):
    ansi.append(int(ansi[-1])+keta[i])

for i in range(len(ansi)-1,0,-1):
    up=ansi[i]//10
    ansi[i]%=10
    ansi[i-1]+=up

if ansi[0]>=10:
    up=ansi[0]//10
    ansi[0]%=10
    ansi.insert(0,up)

ans=map(str,ansi)

print("".join(ans))