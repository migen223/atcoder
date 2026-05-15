
n=int(input())

se=set()
ans=10**10
mas=0
dic={}

for i in range(n):
    score=input().split()
    s=score[0]
    t=int(score[1])
    if s not in se:
        if mas<t:
            mas=t
            ans=i+1
        se.add(s)
print(ans)
