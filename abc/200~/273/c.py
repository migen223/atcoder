from collections import Counter
n=int(input())
a=list(map(int,input().split()))

ac=Counter(a)
ase=list(set(a))
ase.sort()
dic={}
se=set()
for i in range(len(ase)):
    dic[len(ase)-1-i]=ase[i]
    se.add(len(ase)-1-i)

#print(dic)

for i in range(n):
    if i in se:
        print(ac[dic[i]])
    else:
        print(0)

