from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
s=input()
m=[[0]*n for i in range(3)]
x=[[0]*n for i in range(3)]
ml=[]
xl=[]
e=[]
def printout(l):
    for i in range(3):
        print(*l[i])

def mex(a,b,c):
    se=set([a,b,c])
    res=0
    for i in range(5):
        if i not in se:
            res=i
            break
    return res

if s[0]=="M":
    m[a[0]][0]+=1
if s[-1]=="X":
    x[a[-1]][-1]+=1

for i in range(1,n):
    for j in range(3):
        m[j][i]=m[j][i-1]
        x[j][-i-1]=x[j][-i]
    if s[i]=="M":
        m[a[i]][i]+=1
    if s[-1-i]=="X":
        x[a[-i-1]][-i-1]+=1
    if s[i]=="E":
        e.append(i)

for i in range(n):
    if s[i]=="M":
        ml.append(i)
    elif s[i]=="X":
        xl.append(i)

ans=0
for i in range(len(e)):
    mind=bisect_left(ml,e[i])
    xind=bisect_left(xl,e[i])
    if mind==0 or xind==len(xl):
        continue
    mind=ml[mind-1]
    xind=xl[xind]
    m1=[m[0][mind],m[1][mind],m[2][mind]]
    x1=[x[0][xind],x[1][xind],x[2][xind]]
    e1=a[e[i]]
    #print("m1",m1,mind)
    #print("x1",x1,xind)
    #print(e1,e[i])
    for j in range(3):
        for k in range(3):
            ans+=mex(j,e1,k)*(m1[j]*x1[k])
print(ans)
#printout(m)
#printout(x)
    