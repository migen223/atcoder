from itertools import product
n,k,x=map(int,input().split())
words=[]
for i in range(n):
    words.append(input())
ind=[i for i in range(n)]
ansl=[]
for comb in product(ind,repeat=k):
    t=""
    for i in range(k):
        t+=words[list(comb)[i]]
    ansl.append(t)
    #print(list(comb))
ansl.sort()
#print(len(ansl))
print(ansl[x-1])
#print(ansl)
