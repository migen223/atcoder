n=int(input())
a=list(map(int,input().split()))
a_sort=sorted(a)
ruiseki=[0]
now=0
dic={}
for i in a_sort:
    now+=i
    ruiseki.append(now)
for i in range(n-1):
    if a_sort[i]!=a_sort[i+1]:
        dic[a_sort[i]]=i+1

ma=max(a)
for i in range(n):
    if a[i]==ma:
        print(0,end=" ")
    else:
        print(ruiseki[-1]-ruiseki[dic[a[i]]],end=" ")
print()