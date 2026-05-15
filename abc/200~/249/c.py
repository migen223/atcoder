from itertools import product
n,k=map(int,input().split())

words=[input() for i in range(n)]
word=[]
for i in range(n):
    for j in range(len(words[i])):
        word.append(words[i][j])
wordset=[]
for i in range(n):
    s=set()
    for j in range(len(words[i])):
        s.add(words[i][j])
    wordset.append(s)

ans=0
for p in product([0,1],repeat=n):
    dic={}
    count=0
    for i in range(97, 123):
        dic[chr(i)]=0
    for i in  range(n):
        if p[i]==1:
            for j in range(len(words[i])):
                dic[words[i][j]]+=1
    for i in dic:
        if dic[i]==k:
            count+=1
    ans=max(ans,count)
print(ans)



