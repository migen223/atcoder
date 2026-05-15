n,m=map(int,input().split())
a=list(map(int,input().split()))
people=[i for i in range(1,n+1)]
people_quiz=[]

for i in range(n):
    s=input()
    people_quiz.append(s)
    for j in range(m):
        if s[j]=="o":
            people[i]+=a[j]

ma=max(people)
for i in range(n):
    if ma==people[i]:
        print(0)
    else:
        now=people[i]
        unsolve=[]
        for j in range(m):
            if people_quiz[i][j]=="x":
                unsolve.append(a[j])
        unsolve.sort()
        ans=0
        while ma>now:
            now+=unsolve.pop()
            ans+=1
        print(ans)