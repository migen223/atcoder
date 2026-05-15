
n=int(input())

dic={}
for  i in range(n):
    s=input()[0]
    if s not in dic:
        dic[s]=1
    else:
        dic[s]+=1


ans=0
for i in dic:
    ans=max(dic[i],ans)
print(ans)