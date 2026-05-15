
n,r,c=map(int,input().split())
s=input()
dic={"N":[-1,0],"W":[0,-1],"S":[1,0],"E":[0,1]}

ruiseki=[(0,0)]
se=set(ruiseki)
ans=[]
for i in range(n):
    now=dic[s[i]]
    ruiseki.append((ruiseki[-1][0]+now[0],ruiseki[-1][1]+now[1]))
    se.add(ruiseki[-1])
    res=ruiseki[-1]
    if (res[0]-r,res[1]-c) in se:
        ans.append("1")
    else:
        ans.append("0")
        
print("".join(ans))


"""
00100111111000101111
00100111111000101111
"""
