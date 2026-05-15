n=int(input())
s=[]
long=0
for i in range(n):
    l=list(input())
    s.append(l)
    long=(max(long,len(l)))
ansl=[]
for i in range(long):
    q=["*"]*n
    ansl.append(q)
#print(s)
for i in range(n):
    for j in range(len(s[i])):
        ansl[j][n-i-1]=s[i][j]
        #print(j,n-i-1,s[i][j])

for i in range(long):
    for j in range(n):
        if ansl[i][-1]=="*":
            ansl[i].pop()
        else:
            break
for i in range(len(ansl)-1):
    print("".join(ansl[i]))

print("".join(ansl[-1]))
