
n,q=map(int,input().split())
a=list(map(int,input().split()))

dic1={}
dic2={}
for i in range(n):
    if a[i] not in dic2:
        dic2[a[i]]=1
        d={}
        d[1]=i+1
        dic1[a[i]]=d
    else:
        dic2[a[i]]+=1
        dic1[a[i]][dic2[a[i]]]=i+1


#print(dic1)
#print(dic2)

for i in range(q):
    x,k=map(int,input().split())
    if x not in dic2:
        print(-1)
    else:
        if k>dic2[x]:
            print(-1)
        else:
            print(dic1[x][k])