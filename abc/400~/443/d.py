
t=int(input())

for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    ansl=[n+1]*(n)
    dic={}
    for i in range(1,n+1):
        dic[i]=set()
    for i in range(n):
        dic[r[i]].add(i)
    for i in range(1,n+1):
        for j in dic[i]:
            #print("dic",j,dic[i])
            ansl[j]=min(i,ansl[j])
            if 0<=j+1<=n-1 :
                if ansl[j+1]>i+1:
                    dic[i+1].add(j+1)
            if 0<=j-1<=n-1:
                if ansl[j-1]>i+1:
                    dic[i+1].add(j-1)
        #print("ansl",ansl)
    ans=0
    for i in range(n):
        ans+=abs(r[i]-ansl[i])
    #print(ansl)
    print(ans)
