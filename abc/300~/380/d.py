
s=input()
n=len(s)
q=int(input())
c=list(map(int,input().split()))

def count(n):
    n=bin(n)
    ans=0
    for i in range(2,len(n)):
        if n[i]=="1":
            ans+=1
    #print(ans)
    return ans

for i in range(q):
    if c[i]<=n:
        print(s[c[i]-1],end=" ")
    else:
        q=(c[i]-1)//n
        r=(c[i]-1)%n
        if count(q)%2==0:
            print(s[r],end=" ")
        else:
            print(s[r].swapcase(),end=" ")
print()


"""

AC 
a B A b A b a B A b a B a B A b
a B A b A b a B A b a B a B A b 

AC
q q W e t I E Q
q q W e t I E Q 






"""
        
