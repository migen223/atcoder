
n,t,m=map(int,input().split())

fact=[1]
for i in range(1,11):
    fact.append(fact[-1]*i)

team=[]
bad=[set() for i in range(n)]
ans=0
for i in range(m):
    a,b=map(lambda x:int(x)-1,input().split())
    bad[a].add(b)
    bad[b].add(a)


#print(bad)

def solve(teams,p,bla):
    global ans
    #print(teams,p,bla)
    if p<n-1:
        for ti in range(len(teams)):
            if not ((teams[ti]&bad[p])):  
                teams[ti].add(p)
                #print("solve",teams,p+1,bla)
                solve(teams,p+1,bla)
                teams[ti].discard(p)
        #print(teams,"buiaw")
        if len(teams)<t:
            
            teams.append(set([p]))
            #print("oaefhu",teams,p)
            solve(teams,p+1,bla-1)
            teams.pop()
            
    else:
        for ti in range(len(teams)):
            if not ((teams[ti]&bad[p])): 
                teams[ti].add(p) 
                if len(teams)==t:
                    ans+=1
                    #print("ans",teams)
                teams[ti].discard(p)
        if len(teams)<t:
            
            teams.append(set([p]))
            if len(teams)==t:
                ans+=1
            teams.pop()
                


solve(team,0,t)
print(ans)              



"""
team=[]
for p in product(range(t),repeat=n):
    l=[[] for i in range(t)]
    for i in range(n):
        l[p[i]].append(i)
    f=0
    for i in range(t):
        if not l[i]:
            f+=1
            break
    if f==0:
        team.append(l)

def C(n,k):
    return fact[n]//fact[k]//fact[n-k]

one=4
two=C(4,2)*(2**7-2)
three=C(4,3)*(3**7-3-(2**7-2))
print(4**7-one+two+three)

print(len(team))
#for i in range(len(team)):
 #   print(team[i])
    """