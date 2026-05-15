
def z_algorithm(s):
    n=len(s)
    z=[0]*n
    z[0]=n

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
        while k<j and k+z[k]<j:
            z[i+k]=z[k]
            k+=1
        
        i+=k
        j-=k

    return z

t=int(input())

for _ in range(t):
    a=list(input())
    b=list(input())
    n=len(a)
    s=b[:]
    for i in range(2*n):
        s.append(a[i%n])
    z=z_algorithm(s)
    ans=-1
    for i in range(n,3*n):
        if z[i]>=n:
            ans=i-n
            break
    print(ans)
    
    
