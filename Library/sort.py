from functools import cmp_to_key
#特殊な比較によるsort　ABC308 C
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
    
#降順に並べるときは(a,b)を与えたときa>b→-1 a<b→1 1==b 1
#昇順は逆
    
#この場合a/(a+b)が大きい順にソートされる
x=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append((-a,a+b,i))
x.sort(key=cmp_to_key(cmp),reverse=True)