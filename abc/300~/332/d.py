from collections import deque
import sys
h,w=map(int,input().split())

ga=[[] for i  in range(h)]
gb=[[] for _ in range(h)]
dica={}
dicb={}
for i in range(h):
    l=list(map(int,input().split()))
    for j in range(w):
        aij=l[j]
        ga[i].append(aij)
        if aij not in dica:
            dica[aij]=1
        else:
            dica[aij]+=1
for i in range(h):
    l=list(map(int,input().split()))
    for j in range(w):
        bij=l[j]
        gb[i].append(bij)
        if bij not in dicb:
            dicb[bij]=1
        else:
            dicb[bij]+=1

def totuple(g):
    res=[]
    for i in g:
        #print(i)
        res.append(tuple(i))
    return tuple(res)
def tolist(g):
    res=[]
    for i in range(h):
        l=[]
        for j in range(w):
            l.append(g[i][j])
        res.append(l)
    return res

def out(g):
    for i in range(h):
        print(*g[i])
    print()

if dica==dicb:
    vis=set()
    v=deque([([[ga[i][j] for  j in range(w)] for i in range(h)],0)])
    #print("v0",v)
    vis.add(totuple(v[0][0]))
    while v:
        g,dep=v.popleft()
        g=tolist(g)
        """if dep==2:
            print(dep)
            out(g)"""
        if g==gb:
            print(dep)
            #out(g)
            sys.exit()
        for i in range(h-1):
            j=i+1
            for k in range(w):
                g[i][k],g[j][k]=g[j][k],g[i][k]
            t=totuple(g)
            #print(t)
            #out(t)
            if t not in vis:
                #out(g)
                v.append([t,dep+1])
                vis.add(t)
            for k in range(w):
                g[i][k],g[j][k]=g[j][k],g[i][k]

        for i in range(w-1):
            j=i+1
            for k in range(h):
                g[k][i],g[k][j]=g[k][j],g[k][i]
            t=totuple(g)
            #print(t)
            if t not in vis:
                v.append([t,dep+1])
                vis.add(t)
            for k in range(h):
                g[k][i],g[k][j]=g[k][j],g[k][i]
        #print(v)
        #print(vis)
    print(-1)
    
else:
    print(-1)

"""
5 5
710511029 136397527 763027379 644706927 447672230
979861204 57882493 442931589 951053644 152300688
43971370 126515475 962139996 541282303 834022578
312523039 506696497 664922712 414720753 304621362
325269832 191410838 286751784 732741849 806602693

806602693 732741849 286751784 191410838 325269832
304621362 414720753 664922712 506696497 312523039
834022578 541282303 962139996 126515475 43971370
152300688 951053644 442931589 57882493 979861204
447672230 644706927 763027379 136397527 710511029

5 5 
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
1 3 2 4 5
6 7 10 9 8
11 13 15 14 12
19 18 17 20 16
22 23 21 25 24

"""