n=int(input())
a=list(map(int,input().split()))
dic={}
se=set()
for i in range(n):

    if a[i] in se:
        print(dic[a[i]]+1,end=" ")
        dic[a[i]]=i
    else:
        dic[a[i]]=i
        se.add(a[i])
        print(-1,end=" ")
    #print(dic)
    #print(se)
print()