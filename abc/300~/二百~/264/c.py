from itertools import  combinations
import sys
h1,w1=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h1)]
h2,w2=map(int,input().split())
b=[list(map(int,input().split())) for i in range(h2)]

ans=h2*w2
for c1 in combinations(range(h1),h1-h2):
    for c2 in combinations(range(w1),w1-w2):
        hs=set(c1)
        ws=set(c2)
        count=0
        h=0
        w=0
        for i in range(h1):
            if i not in hs:
                w=0
                for j in range(w1):
                    if  j not in ws:
                        #print(i,j,hs,ws,h,w)
                        if a[i][j]==b[h][w]:
                            count+=1
                        w+=1
                h+=1
        if count==ans:
            print("Yes")
            sys.exit()
print("No")
