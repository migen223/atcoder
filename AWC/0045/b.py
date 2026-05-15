import sys
def z_algorithm(s):
    n=len(s)
    z=[0]*n
    i=1
    j=0
    while i<n:
        while i+j<n and s[j]==s[i+j]:
            j+=1
        z[i]=j

        if j==0:
            i+=1
            continue

        k=1
        while (k<j and k+z[k]<j):
            z[i+k]=z[k]
            k+=1
        
        i+=k
        j-=k

    return z

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

b.append("$")
for i in a:
    b.append(i)

#print(b)
z=z_algorithm(b)
#print(z)
for i in range(m+1,len(b)):
    if z[i]==m:
        print(i-m)
        sys.exit()

print(-1)
        