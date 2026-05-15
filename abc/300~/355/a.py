a,b=map(int,input().split())
l=[0,0,0]

if a==b:
    print(-1)
else:
    l[a-1]+=1
    l[b-1]+=1
    for i in range(3):
        if l[i]==0:
            print(i+1)