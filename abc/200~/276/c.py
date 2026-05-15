
n=int(input())
p=list(map(int,input().split()))
if p[-1]<p[-2]:
    p[-1],p[-2]=p[-2],p[-1]
    print(*p)
else:
    ind=1000
    for i in range(n-2):
        if p[-3-i]>p[-2-i]<p[-1-i]:
            ind=-2-i
            break
    l=[]
    for i in range(-ind+1):
        l.append(p.pop())
    mi=100000000
    for i in range(len(l)):
        if l[-1]>l[i]:
            mi=min(mi,l[-1]-l[i])
        #print(mi)
    l.remove(l[-1]-mi)
    p.append(l[-1]-mi)
    l.sort()
    for i in range(-ind):
        p.append(l[-i-1])
    print(*p)
