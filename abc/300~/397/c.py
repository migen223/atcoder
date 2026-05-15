
n=int(input())
a=list(map(int,input().split()))
a1=set([a[0]])
a2=set([a[-1]])

ansl=[[0,0] for i in range(n-1)]
ansl[0][0]=1
ansl[-1][1]=1
for i in range(1,n-1):
    a1.add(a[i])
    a2.add(a[-i-1])
    ansl[i][0]=len(a1)
    ansl[-i-1][1]=len(a2)
big=sum(ansl[0])
#print(f"big={big}")
for i in range(len(ansl)):
    #print(f"sum(ansl[]={sum(ansl[i])}")
    if big<sum(ansl[i]):
        big=sum(ansl[i])
print(big)