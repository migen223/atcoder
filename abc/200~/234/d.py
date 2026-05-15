
n,k=map(int,input().split())
p=list(map(int,input().split()))

number=[0]*(n+1)

first=p[:k]
first.sort(reverse=True)
now=first[k-1]
for i in range(k):
    number[first[i]]=1

print(now)
for i in range(k,n):
    if p[i]>now:
        number[p[i]]=1
        now+=1
        while number[now]==0:
            now+=1
    #print(number)
    print(now)



