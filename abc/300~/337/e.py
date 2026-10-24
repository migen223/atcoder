
n=int(input())
m=1
while 2**m<n:
    m+=1
print(m)

for i in  range(m):
    l=[]
    for j in range(n):
        if (j >> i) & 1:
            l.append(j+1)
    print(len(l),*l)
s=list(input())
s.reverse()
s="".join(s)
print(int(s,2)+1)

"""
n=int(input())
m=(n+1)//2

print(m)
for i in range(m):
    l=[i+j+1 for j in range(n-n//2)]
    print(n-n//2,*l)

s=input()
ans=0
if s[0]=="1":
    for i in range(m):
        if s[i]=="1":
            ans+=1
        else:
            break
else:
    ans=n//2
    for i in range(m):
        if s[i]=="0":
            ans+=1
        else:
            break
    if n%2==1:
        ans+=1
print(ans)


"""

