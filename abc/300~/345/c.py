s=list(input())
ans=len(s)*(len(s)-1)//2
se=set()
dic={}
over2=set()
for i in range(len(s)):
    if s[i] in se:
        dic[s[i]]+=1
        if dic[s[i]]==2:
            over2.add(s[i])
    else:
        dic[s[i]]=1
        se.add(s[i])
#print(dic,se,over2)
for i in over2:
    ans-=dic[i]*(dic[i]-1)//2
if len(over2)!=0:
    ans+=1

print(ans)