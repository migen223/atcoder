
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
aind=[]
bind=[]
a.sort(reverse=True)
b.sort(reverse=True)
count=1
while len(a)*len(b)>0:
    if a[-1]<b[-1]:
        a.pop()
        aind.append(count)
    else:
        b.pop()
        bind.append(count)
    count+=1
    #print(aind)
    #print(bind)
if len(a)==0:
    for i in range(len(b)):
        bind.append(count)
        count+=1
else:
    for i in range(len(a)):
        aind.append(count)
        count+=1
print(*aind)
print(*bind)