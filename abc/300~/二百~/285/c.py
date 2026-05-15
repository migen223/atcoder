s=input()
dic={}
for i in range(65,91):
    dic[chr(i)]=i-64

ans=0
n=len(s)
for i in range(n):
    ans+=dic[s[-1-i]]*(26**i)
print(ans)