
n=int(input())
def ansf(n):
    k=0
    while 2**k<n:
        k+=1
    k-=1
    return int(k*(2**k)+(k+2)*(n-(2**k)))
print(ansf(n))
"""
for i in range(2,n):
    #print(a[i],end=" ")
    #ansf(i)
    if a[i]!=ansf(i):
        print(i,a[i],ansf(i))
        break

def ceil(n):
    if n%2==0:
        return n//2
    else:
        return n//2+1
def floor(n):
    return n//2
a=[0]*(n+1)
a[2]=2
a[3]=5
for i in range(4,n):
    a[i]=i+a[ceil(i)]+a[floor(i)]
dic={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in range(2,n):
    #print(a[i])
    dic[a[i]-a[i-1]]+=1
print(dic)
"""

