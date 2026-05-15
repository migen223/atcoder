from functools import cmp_to_key

n=int(input())

def cmp(a,b):
    c,d,i=a
    e,f,j=b
    left=c*f
    right=e*d
    if left>right:
        return -1
    elif right>left:
        return 1
    else:
        return 0
    

x=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append((a,a+b,i))
x.sort(key=cmp_to_key(cmp))  
#print(x)  
for i in range(n):
    print(x[i][2]+1,end=" ")
"""
bunsi=[]
bunbo=[]
multi=1
for i in range(n):
    a,b=map(int,input().split())
    bunsi.append(a)
    bunbo.append(a+b)
    multi*=(a+b)

tubun=[]
for i in range(n):
    tubun.append(bunsi[i]*(multi//bunbo[i]))

se=set()
dic={}
for i in range(n):
    if tubun[i] not in se:
        dic[tubun[i]]=[i+1]
        se.add(tubun[i])
    else:
        dic[tubun[i]].append(i+1)
l=list(se)
#print(dic)
l.sort(reverse=True)

for i in range(len(l)):
    for j in range(len(dic[l[i]])):
        print(dic[l[i]][j],end=" ")
"""


"""
1 2 3 4 5 
2 3 4 5 6
"""