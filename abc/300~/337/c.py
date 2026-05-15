n=int(input())
a=list(map(int,input().split()))
dic1={}
dic2={}
ans=[]
for i in range(n):
    a[i]-=1

for i in range(n):
    if a[i]==-2:
        ans.append(i)
        second=i+1
    else:
        dic1[a[i]]=i
#print(dic1)
for i in range(n-1):
    #print(ans)
    ans.append(dic1[ans[i]])
for i in range(n):
    ans[i]+=1
print(*ans)

"""
10 17 12 6 4 21 11 24 26 7 30 16 25 2 28 27 20 3 1 8 15 18 5 23 13 22 19 29 9 14
10 17 12 6 4 21 11 24 26 7 30 16 25 2 28 27 20 3 1 8 15 18 5 23 13 22 19 29 9 14

"""