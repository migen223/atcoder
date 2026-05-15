n=int(input())
p=list(map(int,input().split()))
q=int(input())
dic={}
for i in range(n):
    dic[p[i]]=i
for i in range(q):
    a,b=map(int,input().split())
    if dic[a]<dic[b]:
        print(a)
    else:
        print(b)