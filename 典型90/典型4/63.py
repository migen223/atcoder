from collections import Counter
h,w=map(int,input().split())

grid=[list(map(int,input().split())) for _ in range(h)]
ans=-1
for i in range(1 << h): #0から2^Nまで
    l=[]
    for k in range(w):
        res=[]
        for j in reversed(range(h)):
            #print(j)
            # iのjビット目が0なら"(", 1なら")" 
            #print("i=",bin(i),j,i & (1 << j))     
            if (i & (1 << j)) == 0:
                continue
            else:
                
                if len(res)==0:
                    res.append(grid[j][k])
                else:
                    if res[-1]!=grid[j][k]:
                        res.append(grid[j][k])
                        break
                        
        if len(res)==1:
            l.append(res[0])
    if len(l)>=1:
        lc=Counter(l)
        #print(l)
        mc=lc.most_common(1)[0][1]
        #print(mc)
        height=0
        for j in reversed(range(h)):
            if (i & (1 << j)) != 0:
                height+=1
        ans=max(ans,height*mc)

print(ans)