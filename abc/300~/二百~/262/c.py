
n=int(input())
a=list(map(int,input().split()))

correct=0
match=0
dic={}
for i in range(1,n+1):
    dic[i]=a[i-1]
#print(dic)
ans=0
for i in range(1,n+1):
    #print(dic[a[i-1]],a[i-1])
    if a[i-1]==i:
        correct+=1
    else:
        if dic[a[i-1]]==i:
            match+=1
#print(correct,match//2)
ans+=match//2
if correct>=2:
    ans+=correct*(correct-1)//2
print(ans)