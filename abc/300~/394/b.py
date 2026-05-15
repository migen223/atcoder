n=int(input())
word=[]
length=[]
d={}
for i in range(n):
    s=input()
    length.append(len(s))
    word.append(s)
    d[len(s)]=i
length.sort()
ans=""
for i in length:
    ans+=word[d[i]]
print(ans)