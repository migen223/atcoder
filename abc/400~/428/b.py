from collections import Counter
n,k=map(int,input().split())
s=input()
se=set()
dic={}

words=[]
for i in range(n-k+1):
    word=[]
    for j in range(k):
        word.append(s[i+j])
    word="".join(word)
    words.append(word)
c=Counter(words)

tu=c.most_common()
print(tu[0][1])
ma=tu[0][1]
ans=[]
#print(tu)
for i in tu:
    if i[1]==ma:
        ans.append(i[0])
ans.sort()
print(*ans)
