
n=int(input())
a=list(map(int,input().split()))
dic={}
for i in range(n):
    dic[a[i]]=i
a.sort()
print(dic[a[-2]]+1)