from bisect import bisect_left,bisect_right
n,L,R=map(int,input().split())
s=input()

dic={}
for i in range(n):
    if s[i] in dic:
        dic[s[i]].append(i)
    else:
        dic[s[i]]=[i]

ans=0
for l in dic:
    #print(dic[l])
    for i in range(len(dic[l])-1):
        left=bisect_left(dic[l],dic[l][i]+L)
        right=bisect_right(dic[l],dic[l][i]+R)
        #print(dic[l][i],left,right)
        ans+=right-left
print(ans)