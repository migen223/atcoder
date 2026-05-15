n=int(input())
sl=[]
tl=[]
for i in range(n):
    sn=input()
    sl.append(sn)
for i in range(n):
    tn=input()
    tl.append(tn)
#print(sl)
#print(tl)
s=[]
t=[]
for i in range(n):
    for j in range(n):
        #print(f"{i} {j}")
        if sl[i][j]=="#":
            s.append([i,j])
        if tl[i][j]=="#":
            t.append([i,j])
def change(N,l):
    for i in range(len(l)):
        #print(N,l[i][0])
        l[i][0],l[i][1]=l[i][1],N-1-l[i][0]
t_set = set(tuple(x) for x in t)
count=0
ans=999999999
for i in range(4):
    now=count
    right=0
    for j in range(len(s)):
        if tuple(s[j]) not in t_set:
            now+=1
        else:
            right+=1
    now+=len(t)-right
    if ans>now:
        ans=now
    #print(s)
    change(n,s)
    #print(now)
    count+=1
print(ans)