
n,k=map(int,input().split())
a=list(map(int,input().split()))

dic={}
for i in range(n):
    dic[a[i]]=0

allc=k//n
k1=k-k//n*n

asort=sorted(a)
for i in range(k1):
    dic[asort[i]]+=1
for i in range(n):
    print(allc+dic[a[i]])


