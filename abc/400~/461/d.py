from bisect import bisect_left
h,w,K=map(int,input().split())

grid=[[] for _ in range(h)]
r=[[0 for _ in range(w+1)] for _ in range(h+1)]
for i in range(h):
    line=list(input())
    for j in range(w):
        grid[i].append(int(line[j]))
        r[i+1][j+1]=grid[i][j]

for i in range(1,h+1):
    for j in range(1,w+1):
        r[i][j]+=r[i][j-1]
for i in range(1,w+1):
    for j in range(1,h+1):
        r[j][i]+=r[j-1][i]
"""
dic={}
for i in range(1,w+1):
    d={}
    for j in range(1,h+1):
        ij=r[j][i]
        if ij not in d:
            d[ij]=[j]
        else:
            d[ij].append(j)
    dic[i]=d
#print(dic)"""

def check(k,y,x,w,m):
    res=count(y,x,m,w)
    print("k",k,"y",y,"x",x,"w",w,"m",m)
    if res>=k:
        print(y,x,m,w,"=",res)
        return True
    return False

def count(si,sj,ei,ej):
    print(si,sj,ei,sj)
    return r[ei][ej]-r[ei][sj-1]-r[si-1][ej]+r[si-1][sj-1]


def bsearch(k,y,x,w):
    
    l=y-1
    r=h
    print("k",k,"y",y,"x",x,"w",w,"l",l,"r",r)
    while r-l>1:
        
        mid=(l+r)//2
        print("m=",mid)
        if check(k,y,x,w,mid):
            l=mid
        else:
            r=mid
        
    return r

ans=0
for i in range(1,h+1):
    for j in range(1,w+1):
        for wid in range(j,w+1):
            ind1=bsearch(K,i,j,wid)
            ind2=bsearch(K+1,i,j,wid)
            print("ind1,2",ind1,ind2)
            ans+=max(0,ind2-ind1)



print(ans)

