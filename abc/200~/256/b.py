
n=int(input())
a=list(map(int,input().split()))

p=0
l=[]
for i in range(n):
    l.append(0)
    for j in range(len(l)):
        l[j]+=a[i]
    while l[0]>=4 :
        l.pop(0)
        p+=1
        if len(l)==0:
            break
print(p)
